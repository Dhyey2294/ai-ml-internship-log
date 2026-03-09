from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from io import BytesIO


def generate_pdf(data: dict):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    section_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    # Safe field handling
    destination = data.get("destination") or data.get("city_selected", "N/A")
    city = data.get("city_selected", "N/A")
    total_days = data.get("total_days", "N/A")
    budget_level = data.get("budget_level", "N/A")
    total_cost = (
        data.get("total_estimated_cost")
        or data.get("estimated_budget_range")
        or "Not Available"
    )
    preferences = ", ".join(data.get("preferences", []))

    # Title
    elements.append(Paragraph(f"Travel Plan for {city}", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    # Overview Section
    elements.append(Paragraph("Trip Overview", section_style))
    elements.append(Spacer(1, 0.2 * inch))

    overview_data = [
        ["Destination Entered:", destination],
        ["Duration:", f"{total_days} Days"],
        ["Budget Level:", budget_level],
        ["Estimated Cost:", total_cost],
        ["Preferences:", preferences],
    ]

    table = Table(overview_data, colWidths=[170, 320])
    table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])
    )

    elements.append(table)
    elements.append(Spacer(1, 0.4 * inch))

    # Hotels Section
    elements.append(Paragraph("Recommended Hotels", section_style))
    elements.append(Spacer(1, 0.2 * inch))

    hotels = data.get("recommended_hotels") or data.get("hotel_recommendations", [])

    for hotel in hotels:
        elements.append(
            Paragraph(
                f"<b>{hotel.get('name', 'Hotel')}</b><br/>"
                f"Category: {hotel.get('category', 'N/A')}<br/>"
                f"Price per night: {hotel.get('price_range') or hotel.get('price_range_per_night', 'N/A')}<br/>"
                f"Location: {hotel.get('latitude', '')}, {hotel.get('longitude', '')}",
                normal_style
            )
        )
        elements.append(Spacer(1, 0.3 * inch))

    # Itinerary Section
    elements.append(PageBreak())
    elements.append(Paragraph("Day-wise Itinerary", section_style))
    elements.append(Spacer(1, 0.3 * inch))

    for day in data.get("itinerary", []):
        elements.append(
            Paragraph(f"<b>Day {day.get('day')}</b>", styles["Heading3"])
        )
        elements.append(Spacer(1, 0.2 * inch))

        for activity in day.get("activities", []):
            activity_text = (
                f"<b>{activity.get('time', '')}</b><br/>"
                f"{activity.get('place', '')}<br/>"
                f"Category: {activity.get('category', '')}<br/>"
                f"{activity.get('description', '')}"
            )

            if activity.get("estimated_cost"):
                activity_text += f"<br/>Estimated Cost: {activity.get('estimated_cost')}"

            elements.append(Paragraph(activity_text, normal_style))
            elements.append(Spacer(1, 0.25 * inch))

        elements.append(Spacer(1, 0.4 * inch))

    # Travel Tips Section
    elements.append(PageBreak())
    elements.append(Paragraph("Travel Tips", section_style))
    elements.append(Spacer(1, 0.3 * inch))

    tips = data.get("travel_tips", [])
    tips_list = [ListItem(Paragraph(tip, normal_style)) for tip in tips]

    if tips_list:
        elements.append(ListFlowable(tips_list, bulletType="bullet"))

    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer
