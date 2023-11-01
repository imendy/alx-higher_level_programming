$(document).ready(function(){
    $("header").on({
        click: function(){
            $("header").toggleClass("red green");
        }
    });
});
