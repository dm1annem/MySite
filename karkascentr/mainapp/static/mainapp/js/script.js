$(document).ready(function(){

    //анимируем адаптивную иконку в меню
$('.menu-btn').on('click', function(e){
    e.preventDefault;
    $(this).toggleClass('menu-btn_active')
    $('nav ul').slideToggle(500)
})


})