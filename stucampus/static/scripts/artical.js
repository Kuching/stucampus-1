var logoclicktime = 0;
window.onscroll = function(){
	var scrollTop = document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;
    var biaogan = parseInt($(".artical-header").css("height"))*3/4;
	if(scrollTop>=biaogan){
		$(".artical-header").addClass("up");
		$(".blur").hide();
		$(".artical-title").addClass("artical-title-up");
		$(".artical-main").addClass("main-up");
        $(".artical-cover").hide();
	}
	else if(scrollTop<biaogan){
		$(".artical-header").removeClass("up");
		$(".blur").show();
		$(".artical-title").removeClass("artical-title-up");
		$(".artical-main").removeClass("main-up");
        $(".artical-cover").show();
	}
}
$(function(){
    $(".now").css("display","none");
    $("#nav0").removeClass("nav-active");
    setTimeout(function(){
        $(".fixed-logo").css({"transform":"scale(1)","-webkit-transform":"scale(1)"});
        $(".btn").css({"transform":"scale(1)","-webkit-transform":"scale(1)"});
    },500);
    $("#backTop").click(function() {
        $('html, body').animate({
            scrollTop: '0px'
        }, 800);
        $(".fixed-logo").click();
    });
    w = document.body.clientWidth;
    resized(w);
    navcome(nownavid);
    $(".fixed-logo").bind('click',function(){showtools();});
    $(".comment").bind('click',function(){showcommenttools();});
});
function showtools(){
    logoclicktime += 1;
    if(logoclicktime%2 != 0){
        $("#backTop").css("bottom","5.86667rem");
        $("#share").css("bottom","9.6rem");
        $("#discuss").css("bottom","13.33333rem");
        $("#like").css("bottom","17.06667rem");
    }
    else if(logoclicktime%2 == 0){
        $("#backTop").css("bottom","1.6rem");
        $("#share").css("bottom","1.6rem");
        $("#discuss").css("bottom","1.6rem");
        $("#like").css("bottom","1.6rem");
    }
}
function showcommenttools(){
    $(".add-comment").show();
}