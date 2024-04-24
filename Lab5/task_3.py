import justpy as jp

chart_def = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude',
    align: 'left'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model',
    align: 'left'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} km: {point.y}°C'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]

  }]
}"""

# wp = WebPge

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(
        a = wp, text = "Analiza ocen kursów", classes = "text-h3 text-center q-pa-md"
    )

    p1 = jp.QDiv(
        a = wp, text = "Poszczególne wykresy z analizą kursów", classes = "text-h4"
    )

    hc = jp.HighCharts(
        a = wp, options = chart_def
    )

# Zmiana tytułu
    hc.options.title.text = "Changed title"
  
    list_1 = [1, 2, 3]
    list_2 = [12, 1, 20]

# Zmiana daty
    hc.options.series[0].data = list(zip(list_1, list_2))

    return wp

jp.justpy(app)