$(document).ready(function(){

    // Script handling adding and removing of classes
    window.onload = AddRemoveClass();
    window.addEventListener("resize", AddRemoveClass);

    function AddRemoveClass() {
        var windowWidth = $(window).width();

        if (windowWidth >= 530) {
            $('#edit-button').addClass('pull-right').css('margin', '0 15px');
            $('#delete-button').addClass('pull-right').css('margin', '0 15px');
        }
        else {
            $('#edit-button').removeClass('pull-right').css('margin', '10px 20px');
            $('#delete-button').removeClass('pull-right').css('margin', '10px 20px');
        }
    }

    // Script for the carousel
    $('.carousel').carousel({
          interval: 5000
    });
});