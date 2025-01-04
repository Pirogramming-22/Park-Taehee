let timer; 
let elapsedTime = 0; 
let isRunning = false; 
let isChecked = false; 

const timeDisplay = document.getElementById('time-display'); 
const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const resetBtn = document.getElementById('reset-btn');
const mainBottomRecord = document.querySelector('.main-bottom-record'); 
const checkAllBtn = document.querySelector('.ri-checkbox-blank-circle-line'); 
const deleteBtn = document.querySelector('.ri-delete-bin-6-fill'); 

function formatTime(milliseconds) {
    const totalSeconds = milliseconds / 1000; 
    const minutes = Math.floor(totalSeconds / 60); 
    const seconds = Math.floor(totalSeconds % 60); 
    const centiseconds = Math.floor((milliseconds % 1000) / 10); 
    return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}:${String(centiseconds).padStart(2, '0')}`;
}

startBtn.addEventListener('click', () => {
    if (isRunning) return; 
    isRunning = true;
    const startTime = Date.now() - elapsedTime; 
    timer = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        timeDisplay.textContent = formatTime(elapsedTime); 
    }, 10); 
});

stopBtn.addEventListener('click', () => {
    if (!isRunning) return; 
    isRunning = false;
    clearInterval(timer); 

    const record = document.createElement('div'); 
    record.className = 'record-item'; 

    const recordContent = document.createElement('div');
    recordContent.style.display = 'flex'; 
    recordContent.style.alignItems = 'center'; 
    recordContent.style.justifyContent = 'flex-start'; 

    const circleButton = document.createElement('button');
    circleButton.className = 'ri-checkbox-blank-circle-line'; 

    const timeText = document.createElement('span');
    timeText.textContent = formatTime(elapsedTime); 
    timeText.style.margin = '10px'; 
    timeText.style.marginLeft = 'auto'; 
    timeText.style.marginRight = 'auto'; 
    recordContent.appendChild(circleButton); 
    recordContent.appendChild(timeText);
    record.appendChild(recordContent);
    mainBottomRecord.prepend(record);

    circleButton.addEventListener('click', () => {
        if (circleButton.classList.contains('ri-checkbox-blank-circle-line')) {
            circleButton.classList.remove('ri-checkbox-blank-circle-line');
            circleButton.classList.add('ri-checkbox-circle-line');
        } else if (circleButton.classList.contains('ri-checkbox-circle-line')) {
            circleButton.classList.remove('ri-checkbox-circle-line');
            circleButton.classList.add('ri-checkbox-blank-circle-line');
        }
    });
});

checkAllBtn.addEventListener('click', () => {
    const allRecords = document.querySelectorAll('.record-item');
    isChecked = !isChecked;

    allRecords.forEach(record => {
        const circleButton = record.querySelector('.ri-checkbox-blank-circle-line, .ri-checkbox-circle-line');
        if (circleButton) {
            if (isChecked) {
                circleButton.classList.remove('ri-checkbox-blank-circle-line');
                circleButton.classList.add('ri-checkbox-circle-line');
            } else {
                circleButton.classList.remove('ri-checkbox-circle-line');
                circleButton.classList.add('ri-checkbox-blank-circle-line');
            }
        }
    });

    if (isChecked) {
        checkAllBtn.classList.remove('ri-checkbox-blank-circle-line');
        checkAllBtn.classList.add('ri-checkbox-circle-line');
    } else {
        checkAllBtn.classList.remove('ri-checkbox-circle-line');
        checkAllBtn.classList.add('ri-checkbox-blank-circle-line');
    }
});

deleteBtn.addEventListener('click', () => {
    const records = document.querySelectorAll('.record-item');
    
    records.forEach(record => {
        const circleButton = record.querySelector('.ri-checkbox-circle-line'); 
        if (circleButton) {
            record.remove(); 
        }
    });
});

resetBtn.addEventListener('click', () => {
    isRunning = false;
    clearInterval(timer); 
    elapsedTime = 0; 
    timeDisplay.textContent = '00:00:00'; 
    mainBottomRecord.innerHTML = '';
});
