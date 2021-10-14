// Chart options
const options = {
    chart: {
      height: 350,
      type: "line",
      stacked: false
    },
    dataLabels: {
      enabled: false
    },
    colors: ["#FF1654"],
    series: [
      {
        name: "Series A",
        data: [2, 3, 1.5, 2, 5, 3.5, 2]
      }
    ],
    stroke: {
      width: [3],
      curve: 'smooth'
    },
    markers: {
        size: 4,
    },
    plotOptions: {
      bar: {
        columnWidth: "20%"
      }
    },
    xaxis: {
      categories: ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6', 'Jan 7']
    },
    yaxis: [
      {
        axisTicks: {
          show: true
        },
        axisBorder: {
          show: true,
        },
        title: {
          text: "PM 2.5 Concentration",
        }
      }
    ],
    tooltip: {
      shared: false,
      intersect: true,
      x: {
        show: false
      }
    },
    legend: {
      horizontalAlign: "left",
      offsetX: 40
    }
  };
  
  // Init chart
  const chart = new ApexCharts(document.querySelector("#chart"), options);
  
  // Render chart
  chart.render();
  