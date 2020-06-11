import panel as pn

from .layout_templates import (
    layout_0,
    layout_1,
    layout_2,
    layout_3,
    layout_4,
    layout_5,
    layout_6,
    layout_7,
    layout_8,
    layout_9,
    layout_10,
    layout_11,
    layout_12,
)


def is_widget(obj):
    return "widget" in obj.chart_type or obj.chart_type == "datasize_indicator"


class _LayoutBase:
    _layout: str

    def generate_dashboard(self, title, charts, theme):
        tmpl = pn.Template(theme.layout_head + self._layout)
        tmpl.add_panel(
            "title", '<div class="nav-title"> ' + str(title) + "</div>"
        )

        widgets = pn.Column()

        self._apply_themes(charts, theme)
        self._process_widgets(charts, widgets)
        self._process_charts(charts, tmpl)

        tmpl.add_panel("widgets", widgets)
        return tmpl

    def _apply_themes(self, charts, theme):
        for chart in charts.values():
            if hasattr(chart, "apply_theme"):
                chart.apply_theme(theme.chart_properties)

    def _process_widgets(self, charts, widgets):
        for chart in (x for x in charts.values() if is_widget(x)):
            chart.chart.sizing_mode = "scale_both"
            chart.chart.width = 280
            widgets.append(chart.view())

    def _process_charts(self, charts, tmpl):
        raise NotImplementedError()


class Layout0(_LayoutBase):
    _layout = layout_0

    def _process_charts(self, charts, tmpl):
        """
        layout 0
        [1]
        """

        num_of_charts_added = 0

        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = int(round(90 * 1.0)) * 10
                tmpl.add_panel("chart1", chart.view())
            else:
                break


class Layout1(_LayoutBase):
    _layout = layout_1

    def _process_charts(self, charts, tmpl):
        """
        layout 1
        [1]
        [2]
        """

        num_of_charts_added = 0

        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = int(round(90 * 0.66)) * 10
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = int(round(90 * 0.33)) * 10
                tmpl.add_panel("chart2", chart.view())
            else:
                break

        n = 2 - num_of_charts_added

        for i in range(n):
            chart = 2 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout2(_LayoutBase):
    _layout = layout_2

    def _process_charts(self, charts, tmpl):
        """
        layout 2

        [1 2]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 900
                chart.height = 900
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 900
                chart.height = 900
                tmpl.add_panel("chart2", chart.view())
            else:
                break

        n = 2 - num_of_charts_added

        for i in range(n):
            chart = 2 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout3(_LayoutBase):
    _layout = layout_3

    def _process_charts(self, charts, tmpl):
        """
        layout 3
        [1   2]
        [1   3]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 900
                chart.height = 900
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart3", chart.view())
            else:
                break

        n = 3 - num_of_charts_added

        for i in range(n):
            chart = 3 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout4(_LayoutBase):
    _layout = layout_4

    def _process_charts(self, charts, tmpl):
        """
        layout 4
        [1 2 3]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 * 0.33)
                chart.height = int(1600 * 0.33)
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 * 0.33)
                chart.height = int(1600 * 0.33)
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 * 0.33)
                chart.height = int(1600 * 0.33)
                tmpl.add_panel("chart3", chart.view())
            else:
                break

        n = 3 - num_of_charts_added

        for i in range(n):
            chart = 3 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout5(_LayoutBase):
    _layout = layout_5

    def _process_charts(self, charts, tmpl):
        """
        layout 5
        [  1  ]
        [2   3]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = 600
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 300
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            else:
                break

        n = 3 - num_of_charts_added

        for i in range(n):
            chart = 3 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout6(_LayoutBase):
    _layout = layout_6

    def _process_charts(self, charts, tmpl):
        """
        layout 6

        [1  2]
        [3  4]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 800
                chart.height = 450
                tmpl.add_panel("chart4", chart.view())
            else:
                break

        n = 4 - num_of_charts_added

        for i in range(n):
            chart = 4 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout7(_LayoutBase):
    _layout = layout_7

    def _process_charts(self, charts, tmpl):
        """
        layout 7

        [   1   ]
        [2  3  4]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = 600
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart4", chart.view())
            else:
                break

        n = 4 - num_of_charts_added

        for i in range(n):
            chart = 4 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout8(_LayoutBase):
    _layout = layout_8

    def _process_charts(self, charts, tmpl):
        """
        layout 8

        [     1     ]
        [2  3   4  5]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1600
                chart.height = 600
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart4", chart.view())
            elif num_of_charts_added == 5:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart5", chart.view())
            else:
                break

        n = 5 - num_of_charts_added

        for i in range(n):
            chart = 5 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout9(_LayoutBase):
    _layout = layout_9

    def _process_charts(self, charts, tmpl):
        """
        layout 9

        [1  1  2]
        [1  1  3]
        [4  5  6]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = 1200
                chart.height = 600
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart4", chart.view())
            elif num_of_charts_added == 5:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart5", chart.view())
            elif num_of_charts_added == 6:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart6", chart.view())
            else:
                break

        n = 6 - num_of_charts_added

        for i in range(n):
            chart = 6 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout10(_LayoutBase):
    _layout = layout_10

    def _process_charts(self, charts, tmpl):
        """
        layout 10

        [1  2  3]
        [4  5  6]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart4", chart.view())
            elif num_of_charts_added == 5:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart5", chart.view())
            elif num_of_charts_added == 6:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 450
                tmpl.add_panel("chart6", chart.view())
            else:
                break

        n = 6 - num_of_charts_added

        for i in range(n):
            chart = 6 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout11(_LayoutBase):
    _layout = layout_11

    def _process_charts(self, charts, tmpl):
        """
        layout 11

        [  1      2  ]
        [3   4  5   6]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 2)
                chart.height = 600
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 2)
                chart.height = 600
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart4", chart.view())
            elif num_of_charts_added == 5:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart5", chart.view())
            elif num_of_charts_added == 6:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 4)
                chart.height = 300
                tmpl.add_panel("chart6", chart.view())
            else:
                break

        n = 6 - num_of_charts_added

        for i in range(n):
            chart = 6 - i
            tmpl.add_panel("chart" + str(chart), "")


class Layout12(_LayoutBase):
    _layout = layout_12

    def _process_charts(self, charts, tmpl):
        """
        layout 12

        [1  2  3]
        [4  5  6]
        [7  8  9]
        """

        num_of_charts_added = 0
        for chart in (x for x in charts.values() if not is_widget(x)):
            num_of_charts_added += 1
            if num_of_charts_added == 1:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart1", chart.view())
            elif num_of_charts_added == 2:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart2", chart.view())
            elif num_of_charts_added == 3:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart3", chart.view())
            elif num_of_charts_added == 4:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart4", chart.view())
            elif num_of_charts_added == 5:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart5", chart.view())
            elif num_of_charts_added == 6:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart6", chart.view())
            elif num_of_charts_added == 7:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart7", chart.view())
            elif num_of_charts_added == 8:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart8", chart.view())
            elif num_of_charts_added == 9:
                chart.chart.sizing_mode = "scale_both"
                chart.width = int(1600 / 3)
                chart.height = 300
                tmpl.add_panel("chart9", chart.view())
            else:
                break

        n = 9 - num_of_charts_added

        for i in range(n):
            chart = 9 - i
            tmpl.add_panel("chart" + str(chart), "")
