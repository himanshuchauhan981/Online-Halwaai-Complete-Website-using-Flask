$(function(){
    if($( window ).width() <= 770){
        $(".input-group").css({"width":"14vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":"-10px"});
        
        $(".form-group").css({"width":"80vw", "margin-top":"10px"});
        
    }
    else if($( window ).width() < 862){
        $(".input-group").css({"width":"13vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
    }
    else{
        $(".input-group").css({"width":""});
        $("button.btn.btn-default").css({"width":""});
    }
	$.validator.setDefaults({
		highlight: function(element){
			$(element)
			.closest('.form-group')
			.addClass('has-error')
		},
		unhighlight: function(element){
			$(element)
			.closest('.form-group')
			.removeClass('has-error')
		}
	});
});
$(window).resize(function(){
    if($( window ).width() <769){
        $(".input-group").css({"width":"14vw"});
        $("button.btn.btn-default").css({"width":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":"-10px"});
    }
    else if($( window ).width() < 862){
        $(".input-group").css({"width":"13vw"});
        $("button.btn.btn-default").css({"widht":"8vw"});
        $("nav.navbar.navbar-inverse").css({"margin-top":""});
        $(".form-group").css({"width":"", "margin-top":""});
        
    }
    else{
        $(".input-group").css({"width":""});
        $("button.btn.btn-default").css({"widht":""});
        $(".form-group").css({"width":"", "margin-top":""});
        $(".col-sm-4.text-center").css({"left":"13px"});
    }
});
$(function(){
	$.validate({
		rules:
		{	
		    password: "required",
			birthDate: "required",
			weight: {
			    required:true,
			    number:true
			},
			height:  {
			    required:true,
			    number:true
			},
			email: {
				required: true,
				email: true
			}
		},
			messages:{			
				email: {
				required: true,
				email: true
			}
		},
			password: {
				required: " Please enter password"
			},
			birthDate: {
				required: " Please enter birthdate"
			},
			email: {
				required: ' Please enter email',
				email: ' Please enter valid email'
			},
			weight: {
				required: " Please enter your weight",
				number: " Only numbers allowed"
			},
			height: {
				required: " Please enter your height",
				number: " Only numbers allowed"
			}
		})
});