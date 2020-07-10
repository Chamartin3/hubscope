import Chart from 'vue-chartjs';
import { Bar, mixins } from 'vue-chartjs'


export default {
  extends: Bar,
  props: {
    chartData :{ 
      default: null
    }
  },
  watch: {
    chartData:{
      deep: true,
      handler: 'render'
    }
  },
  data () {
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
            gridLines: {
              color: "gray"
            },
            ticks: {
              fontColor: "white",
            }
          }],
          yAxes: [{
            gridLines: {
              // display: false,
              color: "gray",
            },            
            ticks: {
              fontColor: "white",
            }
          }]
        },
        legend: {
          labels: {
            fontColor: 'white'
          }
        }
      }
    }
  },
  methods: {
    render () {
      this.renderChart(this.chartData, this.options)
    }
  },
  mounted () {
    this.render()
  }
}