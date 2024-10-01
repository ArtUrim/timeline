import calendar
from datetime import date

class HighlightedHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, firstweekday=0, highlight_weeks=None, highlight_color="lightblue"):
        """
        Initialize the custom HTMLCalendar with the option to highlight specific weeks.

        :param firstweekday: First day of the week (0=Monday, 6=Sunday)
        :param highlight_weeks: List of week numbers to highlight (1-based indexing)
        :param highlight_color: Color to highlight the weeks
        """
        super().__init__(firstweekday)
        self.highlight_weeks = highlight_weeks if highlight_weeks is not None else []
        self.highlight_color = highlight_color

    def formatweek(self, theweek, weeknumber):
        """
        Return a complete week as a table row.
        Adds week number at the start and applies highlighting to certain weeks.
        """
        week_html = ''
        for d, wd in theweek:
            if d == 0:
                week_html += '<td class="noday">&nbsp;</td>'  # Empty days (outside current month)
            else:
                week_html += f'<td class="day">{d}</td>'
        
        # If this week needs to be highlighted, wrap it in a <tr> with a special class
        if weeknumber in self.highlight_weeks:
            return f'<tr style="background-color:{self.highlight_color};"><th class="weeknum">{weeknumber}</th>{week_html}</tr>\n'
        else:
            return f'<tr><th class="weeknum">{weeknumber}</th>{week_html}</tr>\n'

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s  = '<th class="weeknum">&nbsp;</th>'
        s += ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return '<tr>%s</tr>' % s


    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a month as a table, with week numbers.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        
        # Get weeks for the given month
        weeks = self.monthdays2calendar(theyear, themonth)

        first_week_in_month = date( theyear, themonth, 1 ).isocalendar()[1]
        
        for week_num, week in enumerate(weeks):
            a(self.formatweek(week, week_num + first_week_in_month))
        
        a('</table>')
        a('\n')
        return ''.join(v)

def test():
    # Example usage
    highlight_weeks = [2, 4]  # Highlight the 2nd and 4th weeks
    highlight_color = 'lightgreen'  # Color for highlighting

    cal = HighlightedHTMLCalendar(firstweekday=0, highlight_weeks=highlight_weeks, highlight_color=highlight_color)
    html_calendar = cal.formatmonth(2024, 10)  # Generate HTML for October 2024

    # To display the output, you'd typically write it to an HTML file, but here's a print for clarity:
    print(html_calendar)

    h = cal.formatyear(2024)
    # This would generate an HTML calendar with the 2nd and 4th weeks highlighted in light green.
    with open('cal.html', 'wt' ) as fh:
        fh.write(h)
