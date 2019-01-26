$(function(){
    if($( window ).width() <= 770){
        $(".input-group").css({"width":"14vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":"-10px"});
        $("p.news_offer1, p.news_offer2").css({"font-size":"4vw", "text-align":"center", "margin-left":"5px"});
        $(".col-sm-4.text-center").css({"width":"50vw"});
        $(".form-group").css({"width":"80vw", "margin-top":"10px"});
        $(".mainselection select, button.btn.btn-primary.btn-lg").css({"font-size":"3vw"});
        $(".col-sm-4.text-center").css({"left":"0"});
    }
    else if($( window ).width() < 862){
        $(".input-group").css({"width":"13vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
    }
    else{
        $(".input-group").css({"width":""});
        $("button.btn.btn-default").css({"width":""});
    }
});
$(window).resize(function(){
    if($( window ).width() <769){
        $(".input-group").css({"width":"14vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":"-10px"});
        $("p.news_offer1, p.news_offer2").css({"font-size":"3vw", "margin-left":"5px", "text-align":"center"});
        $(".col-sm-4.text-center").css({"width":"50vw"});
        $(".form-group").css({"width":"80vw", "margin-top":"10px"});
        $(".mainselection select, button.btn.btn-primary.btn-lg").css({"font-size":"3vw"});
        $(".col-sm-4.text-center").css({"left":"0"});
    }
    else if($( window ).width() < 862){
        $(".input-group").css({"width":"13vw"});
        $("button.btn.btn-default").css({"widht":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":""});
        $("p.news_offer1, p.news_offer2").css({"font-size":"", "text-align":"", "margin-left":""});
        $(".col-sm-4.text-center").css({"width":""});
        $(".form-group").css({"width":"", "margin-top":""});
        $(".mainselection select, button.btn.btn-primary.btn-lg").css({"font-size":""});
        $(".col-sm-4.text-center").css({"left":"13px"});
    }
    else{
        $(".input-group").css({"width":""});
        $("button.btn.btn-default").css({"widht":""});
        $("p.news_offer1, p.news_offer2").css({"font-size":"", "text-align":"", "margin-left":"-90px"});
        $(".col-sm-4.text-center").css({"width":""});
        $(".form-group").css({"width":"", "margin-top":""});
        $(".mainselection select, button.btn.btn-primary.btn-lg").css({"font-size":""});
        $(".col-sm-4.text-center").css({"left":"13px"});
    }
});
