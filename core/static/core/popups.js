const popupLinks = document.querySelectorAll('.popup-link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll('.lock-padding');

let unlock = true;

const timeout = 800;

if (popupLinks.length > 0){
	for(let index = 0; index < popupLinks.length; index++){
		const popupLink = popupLinks[index];
		popupLink.addEventListener("click", function (e){
			const popupName = popupLink.getAttribute('href').replace('#', '');
			const currentPopup = document.getElementById(popupName);
			popupOpen(currentPopup);
			changeBlocks()
			e.preventDefault();
		});
	}
}

const popupCloseIcon = document.querySelectorAll('.close-popup');
if (popupCloseIcon.length > 0){
	for (let index = 0; index < popupCloseIcon.length; index++) {
		const el = popupCloseIcon[index];
		el.addEventListener('click', function (e) {
			popupClose(el.closest('.popup'));
			e.preventDefault();
		} );
	}
}

function popupOpen(currentPopup){
	if (currentPopup && unlock){
		const popupActive = document.querySelector('.popup.open');
		if (popupActive) {
			popupClose(popupActive, false);
		}
		else {
			bodyLock();
		}
		currentPopup.classList.add('open');
		currentPopup.addEventListener("click", function (e) {
			if (!e.target.closest('.popup__content')){
				popupClose(e.target.closest('.popup'));
			}
		});
	}
}

function bodyUnlock() {
	setTimeout(function () {
		if (lockPadding.length > 0) {
			for (let index = 0; index < lockPadding.length; index++) {
				const el = lockPadding[index];
				el.style.paddingRight = '0px';
			}
		}
		body.style.paddingRight = '0px';
		body.classList.remove('lock');
	}, timeout);

	unlock = false;
	setTimeout(function () {
		unlock = true;
	}, timeout);
}

function popupClose(popupActive, doUnlock = true){
	if (unlock) {
		popupActive.classList.remove('open');
		if (doUnlock) {
			bodyUnlock();
		}
	}
}

function changeBlocks(){
	$('#start_left_block').css("display","none");
	$('#start_right_block').css("display","none");
	$('#game_left_block').css("display","block");
	$('#game_right_block').css("display","block");
}

function bodyLock() {
	if (lockPadding.length > 0) {
		for (let index = 0; index < lockPadding.length; index++){
			const el = lockPadding[index];
		}
	}
	body.classList.add('lock');

	unlock = false;
	setTimeout(function () {
		unlock = true;
	}, timeout);
}

document.addEventListener('keydown', function (e){
	if (e.which === 27) {
		const popupActive = document.querySelector('.popup.open');
		popupClose(popupActive);
	}
});

function setRotation(deg) {
	localStorage.setItem('rotation', deg);
	return deg;
}

function rotate(deg) {
	let rotation = parseInt(localStorage.getItem('rotation'));
	rotation = (rotation + deg) % 360;
	localStorage.setItem('rotation', rotation);
	return rotation;
}

async function move(path) {
	const img = document.querySelector('.turtle');
	let	 td = document.querySelector('.with-turtle');
	for(let c = 0; c < path.length; ++c) {
		if (c > 0 && path[c][0] == path[c-1][0] && path[c][1] == path[c-1][1]) {
			rotation = 0;
			if (path[c][2][0] == path[c-1][2][1] && path[c][2][1] == -path[c-1][2][0]) {
				rotation = rotate(90);
			} else {
				rotation = rotate(-90);
			}
			img.style.transform = `rotate(${rotation}deg)`;
		} else {
			const i = path[c][0];
			const j = path[c][1];
			td.removeChild(img);
			td.classList.remove('with-turtle');
			td = document.getElementsByClassName(`i=${i}j=${j}`)[0];
			td.classList.add('with-turtle');
			td.appendChild(img);
			localStorage.setItem('img_x', j);
			localStorage.setItem('img_y', i);
		}
		await new Promise(r => setTimeout(r, 500));
	}
}

function initGrid(level_data) {
	const table = document.querySelector('tbody');
	table.textContent = ''
	const grid = level_data.grid;
	const rate_w = table.clientWidth / grid.length;
	const rate_h = table.clientHeight / grid[0].length;
	const rate = 80 / Math.max(grid.length, grid[0].length);
	let sz;
	if (rate_w > rate_h) {
		sz = `${rate}vw`;
	} else {
		sz = `${rate}vh`;
	}
	for (let i = 0; i < grid[0].length; ++i) {
		const tr = table.insertRow();
		for (let j = 0; j < grid.length; ++j) {
			const td = tr.insertCell();
			td.classList.add(`i=${i}j=${j}`);
			td.style.width = sz;
			td.style.height = sz;
			if (grid[i][j] == 'BARRIER') {	
				td.style.background = 'black';
			}
			if (i == level_data.x_start && j == level_data.y_start) {
				img = document.createElement("img");
				img.src = "https://www.pngall.com/wp-content/uploads/8/Green-Turtle-PNG-Free-Download.png";
				img.style.width = '100%';
				img.style.height = '100%';
				setRotation(90);
				img.style.transform = 'rotate(90deg)';
				img.classList.add(`turtle`);
				localStorage.setItem('img_x', j);
				localStorage.setItem('img_y', i);
				td.appendChild(img)
				td.classList.add('with-turtle')
			} else if (i == level_data.x_finish && j == level_data.y_finish) {
				img = document.createElement("img");
				img.src = "https://www.pngall.com/wp-content/uploads/4/Orange-Flag-PNG.png";
				img.style.width = '100%';
				img.style.height = '100%';
				img.classList.add(`flag`);
				td.appendChild(img)
			}
		}
	}
}	
  
document.querySelectorAll('.lvl-1').forEach(function(el) {
	el.onclick = function() {
		$.getJSON('/level', {'lvl': 1}, function(data, jqXHR){
			localStorage.setItem('lvl_num', data.number);
			localStorage.setItem('x_start', data.x_start);
			localStorage.setItem('y_start', data.y_start);
			localStorage.setItem('x_finish', data.x_finish);
			localStorage.setItem('y_finish', data.y_finish);
			initGrid(data);
		});
	}
}) 

document.querySelectorAll('.lvl-2').forEach(function(el) {
	el.onclick = function() {
		$.getJSON('/level', {'lvl': 2}, function(data, jqXHR){
			localStorage.setItem('lvl_num', data.number);
			localStorage.setItem('x_start', data.x_start);
			localStorage.setItem('y_start', data.y_start);
			localStorage.setItem('x_finish', data.x_finish);
			localStorage.setItem('y_finish', data.y_finish);
			initGrid(data);
		});
	}
}) 

document.querySelectorAll('.lvl-3').forEach(function(el) {
	el.onclick = function() {
		$.getJSON('/level', {'lvl': 3}, function(data, jqXHR){
			localStorage.setItem('lvl_num', data.number);
			localStorage.setItem('x_start', data.x_start);
			localStorage.setItem('y_start', data.y_start);
			localStorage.setItem('x_finish', data.x_finish);
			localStorage.setItem('y_finish', data.y_finish);
			initGrid(data);
		});
	}
}) 

document.getElementById('btn-start').onclick = async function() {
	const text = document.getElementById("code_block").value;
	const lvl_num = localStorage.getItem('lvl_num');
	if (!lvl_num) {
		errorBlock.value = "You need to choose level";
	} else {
		let data;
		await $.getJSON('/path', {'lvl': lvl_num, 'code': text}, function(d, jqXHR){
			data = d;
		});
		errorBlock = document.getElementById('error_block');
		if (data.syntax_error) {
			errorBlock.value = "Syntax is incorrect";
		} else {
			await move(data.path);
			if (data.is_win) {
				errorBlock.value = "";
			} else {
				errorBlock.value = "Your solution is incorrect";
			}
		}
	}
}

document.getElementById("code_block").onclick = async function() {
	const x_start = localStorage.getItem('x_start');
	const y_start = localStorage.getItem('y_start');
	const img_x = localStorage.getItem('img_x');
	const img_y = localStorage.getItem('img_y');
	if (x_start && y_start && img_x && img_y) {
		if (x_start != img_x || y_start != img_y) {
			setRotation(90);
			document.querySelector('.turtle').style.transform = 'rotate(90deg)';
			await move([[x_start, y_start]]);
		}
	}
}
