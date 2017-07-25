function showPopup(url) {
  var left = (screen.width/2)-250;
  var top = (screen.height/2)-250;
  var new_window = window.open(url, 'Youtube', 'resizable=1,statusbars=0,menubars=0,titlebar=0,toolbars=0,width=500,height=500,left='+left+',top='+top);
  new_window.focus();
}

function coverResize() {
    $('#albumCover').height($('.panel').height());
    $('#albumCover').width($('.col-sm-4').width());
}