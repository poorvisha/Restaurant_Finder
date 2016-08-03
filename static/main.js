/**
 * Created by yiping on 2016/8/2.
 */
$(document).ready(function(){
    'use strict';
    //$('.selectpicker').selectpicker({
        //style: 'btn-success',
        //size: 4
    //});
    
    var sf = $('#sf');
    var sj = $('#sj');
    var lv = $('#lv');
    var la = $('#la');
    var sfPic = $('#sfPic');
    var sjPic = $('#sjPic');
    var lvPic = $('#lvPic');
    var laPic = $('#laPic');
    
    sf.click(function(){
        sjPic.removeClass('my-display');
        lvPic.removeClass('my-display');
        laPic.removeClass('my-display');
        sjPic.addClass('my-hide');
        lvPic.addClass('my-hide');
        laPic.addClass('my-hide');
        sfPic.removeClass('my-hide');
        sfPic.addClass('my-display');
    });
    
    
    
    
    
    
});