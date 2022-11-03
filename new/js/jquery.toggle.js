$(function() {
// アコーディオンメニュー
  $('nav > ul > li').on('click', function() {
    $(this).children('ul:not(:animated)').slideToggle();
    $(this).children('span').toggleClass('open');
    $('.sub-menu').not($(this).children('.sub-menu')).slideUp(),
    $('nav li').children('span').not($(this).children('span')).removeClass('open');
  });
});