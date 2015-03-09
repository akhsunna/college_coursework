$( function() {
  $('.js-closeable').on('click', function(e) {
    var $wrapper = $($(this).closest('li'));
    if (!$wrapper.hasClass('close')) {
      $wrapper.height('');
    }
    else {
      $wrapper.height($wrapper.attr('data-height'));
    }
    $wrapper.toggleClass('close');
  }).height('auto').each(function() {
    $wrapper.attr('data-height', $wrapper.height());
  }).height('');
});