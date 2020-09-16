import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bar,
  props: {
    chartData: {
      default: null
    },
    text_color: {
      default: 'white'
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler: 'render'
    }
  },
  data () {
    return {
      options: {
        scales: {
          xAxes: [{
            gridLines: {
              color: 'gray'
            },
            ticks: {
              fontColor: this.text_color
            }
          }],
          yAxes: [{
            gridLines: {
              // display: false,
              color: 'gray'
            },
            ticks: {
              fontColor: this.text_color
            }
          }]
        },
        legend: {
          labels: {
            fontColor: this.text_color
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
    if (this.chartData) this.render()
  }
}
