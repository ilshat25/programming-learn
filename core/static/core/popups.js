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

const grid = document.querySelector('table');
function gridCreate() {
	const c = document.querySelector('table');
	$.getJSON('/level', {lvl: 3}, function(data, jqXHR){
		const rate_w = c.clientWidth / data.length;
		const rate_h = c.clientHeight / data[0].length;
		const rate = 80 / Math.max(data.length, data[0].length);
		let sz;
		if (rate_w > rate_h) {
			sz = `${rate}vw`;
		} else {
			sz = `${rate}vh`;
		}
		for (let i = 0; i < data.length; ++i) {
			const tr = grid.insertRow();
			for (let j = 0; j < data[i].length; ++j) {
				const td = tr.insertCell();
				td.classList.add(`i=${i}j=${j}`);
				td.style.width = sz;
				td.style.height = sz;
				// td.appendChild(document.createTextNode(` `));
				if (data[i][j] == 1) {	
					td.style.background = 'black';
				}
				if (i == 1 && j == 1) {
					img = document.createElement("img");
					img.src = "https://www.pngall.com/wp-content/uploads/8/Green-Turtle-PNG-Free-Download.png";
					img.style.width = '100%';
					img.style.height = '100%';
					img.classList.add(`turtle`);
					td.appendChild(img)
					td.classList.add('with-turtle')
				}
			}
		}
	});
}	
  
gridCreate();
// window.onresize = gridCreate

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

function popupClose(popupActive, doUnlock = true){
	if (unlock) {
		popupActive.classList.remove('open');
		if (doUnlock) {
			bodyUnLock();
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

document.addEventListener('keydown', function (e){
	if (e.which === 27) {
		const popupActive = document.querySelector('.popup.open');
		popupClose(popupActive);
	}
});

document.querySelector('.btn-success').onclick = async function() {
	console.log('click');
	let data;
	await $.getJSON('/path', {}, function(d, jqXHR){
		console.log(d);
		data = d;
	});
	console.log(data);
	const img = document.querySelector('.turtle');
	let	 td = document.querySelector('.with-turtle');
	console.log(img, td);
	for(let c = 0; c < data.length; ++c) {
		const i = data[c][0];
		const j = data[c][1];
		console.log(`i=${i} j=${j}`);
		td.removeChild(img);
		td.classList.remove('with-turtle');
		td = document.getElementsByClassName(`i=${i}j=${j}`)[0];
		console.log(td)
		td.classList.add('with-turtle');
		td.appendChild(img);
		await new Promise(r => setTimeout(r, 500));
	}
}