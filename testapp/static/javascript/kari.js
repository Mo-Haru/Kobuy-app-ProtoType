const $wrap = document.querySelector('.number-spinner-wrap')
const $input = $wrap.querySelector('input')
$wrap.querySelector('.spinner-down').onclick = ()=>{
  $input.stepDown()
}
$wrap.querySelector('.spinner-up').onclick = ()=>{
  $input.stepUp()
}