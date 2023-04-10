'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
  // [ revenue-scroll ] start
  new SimpleBar(document.querySelector('.revenue-scroll'));
  new SimpleBar(document.querySelector('.customers-scroll'));
});

function floatchart() {
  (function () {
    var options1 = {
      chart: {
        type: 'area',
        height: 270,
        sparkline: {
          enabled: false
        }
      },
      colors: ['#673ab7', '#2196f3', '#f44336'],
      stroke: {
        curve: 'smooth',
        width: 2
      },
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          opacityFrom: 0.5,
          opacityTo: 0,
          stops: [0, 80, 100]
        }
      },
      series: [
        {
          name: 'NA',
          data: [10, 90, 65, 85, 40, 80, 45]
        },
        {
          name: 'EU',
          data: [50, 30, 25, 15, 5, 10, 10]
        },
        {
          name: 'APAC',
          data: [25, 50, 40, 55, 20, 40, 25]
        }
      ],
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        title: {
          text: 'Month'
        }
      },
      yaxis: {
        title: {
          text: 'Deals closed'
        }
      },
      legend: {
        position: 'top',
        horizontalAlign: 'center'
      },
      tooltip: {
        fixed: {
          enabled: false
        },
        x: {
          title: {
            show: true
          }
        },
        y: {
          title: {
            show: true,
          }
        },
        marker: {
          show: true
        }
      }
    };
    new ApexCharts(document.querySelector('#account-chart'), options1).render();
  })();
}
