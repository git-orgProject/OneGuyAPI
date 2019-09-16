//获取标签的对象
var box = document.getElementById("box");
var pic = document.getElementById("pic");
var liArr = document.getElementsByTagName("li");
var leftBtn = document.getElementById("left");
var rightBtn = document.getElementById("right");

//设置第一个小圆点被选中，背景色为红色
// liArr[0].style.backgroundColor = "ghostwhite";
liArr[0].style.cssText = "background-color: rgba(0,0,0,0.3); width: 17px;height: 17px;";


//定义一个变量，记录图片
currentPage = 1;


//开启定时器，更换图片，更换小圆点的选中状态
var timer = setInterval(startloop,2000);
function startloop(){
	//递增currentPage，改变图片
	currentPage++;
	changeImage();
	
}

function changeImage(){
	//边界校验
	if(currentPage == 5){
		currentPage = 1;
	}
	
	if(currentPage == 0){
		currentPage = 4;
	}
	
	//更改pic的图片
	pic.src = "img/" + currentPage + ".jpg";
	
	
	//清除之前的设置
	for(var i =0;i < liArr.length;i++){
		liArr[i].style.cssText = "width: 15px;height: 15px;";
	}
	
	//更改小圆点的选中状态
	// liArr[currentPage - 1].style.backgroundColor = "ghostwhite";
	// liArr[currentPage - 1].style.backgroundColor = "rgba(0,0,0,0.2)";
	liArr[currentPage - 1].style.cssText = "background-color: rgba(0,0,0,0.3); width: 17px;height: 17px;";
}

// //鼠标进入box，设置按钮显示出来
// box.addEventListener("mouseover",overfunc,false);
// function overfunc(){
// 	//停止定时器
// 	clearInterval(timer);
// 	
// 	//显示左右按钮
// 	leftBtn.style.display = "block";
// 	rightBtn.style.display = "block";
// }
// 
// //鼠标移出box，设置按钮隐藏，让定时器接着工作
// box.addEventListener("mouseout",outfunc,false);
// function outfunc(){
// 	//恢复定时器
// 	timer = setInterval(startloop,2000);
// 	
// 	//隐藏左右按钮
// 	leftBtn.style.display = "none";
// 	rightBtn.style.display = "none";
// }
// 
// //鼠标进入左右按钮
// //注意：如果多个对象触发同一个事件，则通过this区分当前正在触发事件的对象是哪个
// leftBtn.addEventListener("mouseover",deepFunc,false);
// rightBtn.addEventListener("mouseover",deepFunc,false);
// function deepFunc(){
// 	this.style.backgroundColor = "rgba(0,0,0,0.6)";
// }
// 
// //鼠标移出左右按钮
// leftBtn.addEventListener("mouseout",nodeepFunc,false);
// rightBtn.addEventListener("mouseout",nodeepFunc,false);
// function nodeepFunc(){
// 	this.style.backgroundColor = "rgba(0,0,0,0.2)";
// }
// 
// //点击左右按钮
// leftBtn.addEventListener("click",function(){
// 	currentPage--;
// 	changeImage();
// 	
// },false);
// rightBtn.addEventListener("click",function(){
// 	currentPage++;
// 	changeImage();
// },false);
// 
// //鼠标进入小圆点
// for(var i = 0;i < liArr.length;i++){
// 	//给每个li标签做标记
// 	liArr[i].index = i + 1;
// 	
// 	liArr[i].addEventListener("mouseover",function(){
// 		currentPage = this.index;
// 		changeImage();
// 	},false);
// }
// 


