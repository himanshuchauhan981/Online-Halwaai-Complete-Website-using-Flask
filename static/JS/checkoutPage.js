$(document).ready(function(){
    $("button").click(function(){
        $(this).closest('tr').remove()
    });
});
$(document).ready(function(){
    $("button").click(function(){
        $('p').css({"background-color":"yellow", "font-size":"200%"});
    });
});