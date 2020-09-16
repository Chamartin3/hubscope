const Tipos = [
  // {
  //   value: 'S',
  //   name: 'Simple',
  //   desc: 'Cada registro suma al valor total',
  //   componentes:['value']
  // },
  {
    value: 'A',
    name: 'Acumulado',
    componentes: [
      { name: 'Métrica a acumular', value: 'value' }
    ],
    desc: 'valor que acumula'
  },
  {
    value: 'C',
    name: 'Cociente',
    componentes: [
      { name: 'Métrica a dividir', value: 'numerator' },
      { name: 'Métrica Divisora', value: 'denominator' }
    ],
    desc: 'División entre 2 factores'
  },
  {
    value: 'P',
    name: 'Porcentaje',
    componentes: [
      { name: 'Métrica a dividir', value: 'numerator' },
      { name: 'Métrica Divisora', value: 'denominator' }
    ],
    desc: 'División multiplicada por 100'
  },
  {
    value: 'E',
    name: 'Estado',
    componentes: [
      { name: 'Métrica', value: 'value' }
    ],
    desc: 'valor que reemplaza'
  }
  // {
  //   value: 'SA',
  //   name: 'Producto',
  //   componentes: null,
  //   // Puede ser una suma o una resta
  //   desc: 'Suma Algebraica'
  // }

]

export {
  Tipos
}
