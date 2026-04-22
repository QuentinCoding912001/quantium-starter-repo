from pathlib import Path
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
file_path = Path("formatted_sales_data.csv")
df = pd.read_csv(file_path)

# Parse mixed date formats safely
df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")

# Drop invalid dates
df = df.dropna(subset=["Date"])

# Standardize region values
df["Region"] = df["Region"].astype(str).str.strip().str.lower()

# Define price increase date
price_increase_date = pd.Timestamp("2021-01-15")

# Create app
app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f4f6f8",
        "padding": "30px",
        "minHeight": "100vh"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "25px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "maxWidth": "1200px",
                "margin": "0 auto"
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    id="app-header",
                    style={
                        "textAlign": "center",
                        "marginBottom": "5px",
                        "color": "#1f2937"
                    }
                ),
                html.H4(
                    "By Quentin Bombande",
                    style={
                        "textAlign": "center",
                        "color": "#6b7280",
                        "marginTop": "0",
                        "marginBottom": "30px"
                    }
                ),

                html.Div(
                    [
                        html.Label(
                            "Filter by Region:",
                            style={
                                "fontWeight": "bold",
                                "fontSize": "18px",
                                "display": "block",
                                "marginBottom": "10px",
                                "color": "#111827"
                            }
                        ),
                        dcc.RadioItems(
                            id="region-picker",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            labelStyle={
                                "marginRight": "20px",
                                "fontSize": "16px",
                                "cursor": "pointer"
                            },
                            style={"marginBottom": "30px"}
                        )
                    ]
                ),

                html.Div(
                    id="summary-cards",
                    style={
                        "display": "flex",
                        "justifyContent": "space-between",
                        "gap": "15px",
                        "flexWrap": "wrap",
                        "marginBottom": "30px"
                    }
                ),

                html.Div(
                    id="business-insight",
                    style={
                        "padding": "18px",
                        "borderRadius": "10px",
                        "backgroundColor": "#eef2ff",
                        "border": "1px solid #c7d2fe",
                        "marginBottom": "30px",
                        "color": "#1e3a8a"
                    }
                ),

                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)


def card_style():
    return {
        "flex": "1",
        "minWidth": "220px",
        "backgroundColor": "white",
        "padding": "20px",
        "borderRadius": "10px",
        "border": "1px solid #e5e7eb",
        "boxShadow": "0 2px 8px rgba(0,0,0,0.05)",
        "textAlign": "center"
    }


@app.callback(
    Output("sales-line-chart", "figure"),
    Output("summary-cards", "children"),
    Output("business-insight", "children"),
    Input("region-picker", "value")
)
def update_dashboard(selected_region):
    # Filter dataset
    if selected_region == "all":
        filtered_df = df.copy()
        region_title = "All Regions"
    else:
        filtered_df = df[df["Region"] == selected_region].copy()
        region_title = selected_region.capitalize()

    # Group by date for chart
    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()
    daily_sales = daily_sales.sort_values("Date")

    # Split before and after price increase
    before_data = daily_sales[daily_sales["Date"] < price_increase_date]
    after_data = daily_sales[daily_sales["Date"] >= price_increase_date]

    # Safe calculations
    before_avg = before_data["Sales"].mean() if not before_data.empty else 0
    after_avg = after_data["Sales"].mean() if not after_data.empty else 0
    difference = after_avg - before_avg if (before_avg or after_avg) else 0
    percent_change = ((difference / before_avg) * 100) if before_avg != 0 else 0

    # Line chart
    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time — {region_title}",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        template="plotly_white",
        title_x=0.5
    )

    fig.update_traces(line=dict(width=3))

    fig.add_vline(
        x="2021-01-15",
        line_width=2,
        line_dash="dash",
        line_color="red"
    )

    max_y = daily_sales["Sales"].max() if not daily_sales.empty else 0

    fig.add_annotation(
        x="2021-01-15",
        y=max_y,
        text="Price Increase: Jan 15, 2021",
        showarrow=True,
        arrowhead=1
    )

    # Summary cards
    cards = [
        html.Div(
            [
                html.H3("Average Before", style={"marginBottom": "10px", "color": "#374151"}),
                html.P(f"{before_avg:,.2f}", style={"fontSize": "24px", "fontWeight": "bold", "margin": "0"})
            ],
            style=card_style()
        ),
        html.Div(
            [
                html.H3("Average After", style={"marginBottom": "10px", "color": "#374151"}),
                html.P(f"{after_avg:,.2f}", style={"fontSize": "24px", "fontWeight": "bold", "margin": "0"})
            ],
            style=card_style()
        ),
        html.Div(
            [
                html.H3("Percentage Change", style={"marginBottom": "10px", "color": "#374151"}),
                html.P(f"{percent_change:.2f}%", style={"fontSize": "24px", "fontWeight": "bold", "margin": "0"})
            ],
            style=card_style()
        )
    ]

    # Business insight text
    insight = html.Div([
        html.H3("Business Insight", style={"marginTop": "0"}),
        html.P(
            f"For {region_title}, average daily sales changed from {before_avg:,.2f} before the price increase "
            f"to {after_avg:,.2f} after the increase, representing a change of {percent_change:.2f}%. "
            f"This helps show whether the price increase was associated with higher or lower overall sales in that region."
        )
    ])

    return fig, cards, insight


if __name__ == "__main__":
    app.run(debug=True)