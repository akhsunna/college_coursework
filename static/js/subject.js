$( function() {
  $('.closeable').on('click', function(e) {
    if (!$(this).hasClass('close')) {
      $(this).height('');
    }
    else {
      $(this).height($(this).attr('data-height'));
    }
    $(this).toggleClass('close');
  }).height('auto').each(function() {
    $(this).attr('data-height', $(this).height());
  }).height('');
});