$(document).ready(function(){

    // Script handling adding and removing of classes
    window.onload = AddRemoveClass();
    window.addEventListener("resize", AddRemoveClass);

    function AddRemoveClass() {
        var windowWidth = $(window).width();

        if (windowWidth >= 400) {
            $('#edit-button').addClass('pull-right').css('display', 'inline-block');
        }
        else {
            $('#edit-button').removeClass('pull-right').css('display', 'inline');
        }
    }

    // Script for the carousel
    $('.carousel').carousel({
          interval: 5000
    });
});