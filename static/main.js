/**
 * Created by yiping on 2016/8/2.
 */
$(document).ready(function() {
  'use strict';
  
  var city = $('#city');
  var sfPic = $('#sfPic');
  var sjPic = $('#sjPic');
  var lvPic = $('#lvPic');
  var laPic = $('#laPic');
  
  city.change(function() {
    var value = $(this).val();
    console.log(value);
    if (value === 'San Francisco') {
      console.log('sf is good');
      sjPic.removeClass('my-display');
      lvPic.removeClass('my-display');
      laPic.removeClass('my-display');
      sjPic.addClass('my-hide');
      lvPic.addClass('my-hide');
      laPic.addClass('my-hide');
      sfPic.removeClass('my-hide');
      sfPic.addClass('my-display');
    }
    
    if (value === 'San Jose') {
      sfPic.removeClass('my-display');
      lvPic.removeClass('my-display');
      laPic.removeClass('my-display');
      sfPic.addClass('my-hide');
      lvPic.addClass('my-hide');
      laPic.addClass('my-hide');
      sjPic.removeClass('my-hide');
      sjPic.addClass('my-display');
    }
    
    if (value === 'Las Vegas') {
      sjPic.removeClass('my-display');
      sfPic.removeClass('my-display');
      laPic.removeClass('my-display');
      sjPic.addClass('my-hide');
      sfPic.addClass('my-hide');
      laPic.addClass('my-hide');
      lvPic.removeClass('my-hide');
      lvPic.addClass('my-display');
    }
    
    if (value === 'Los Angeles') {
      sjPic.removeClass('my-display');
      lvPic.removeClass('my-display');
      sfPic.removeClass('my-display');
      sjPic.addClass('my-hide');
      lvPic.addClass('my-hide');
      sfPic.addClass('my-hide');
      laPic.removeClass('my-hide');
      laPic.addClass('my-display');
    }
    
    
  });
  
  
});