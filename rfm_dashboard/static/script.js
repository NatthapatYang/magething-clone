document.addEventListener('DOMContentLoaded', function() {
    const rButton = document.getElementById('r_button');
    const fButton = document.getElementById('f_button');
    const mButton = document.getElementById('m_button');
    const recencyDiv = document.getElementById('recency');
    const frequencyDiv = document.getElementById('frequency');
    const monetaryDiv = document.getElementById('monetary');

    rButton.style.backgroundColor = 'rgb(239, 68, 68)'; 

    rButton.addEventListener('click', function() {
        recencyDiv.style.display = 'block'; 
        frequencyDiv.style.display = 'none';
        monetaryDiv.style.display = 'none';
        fButton.style.backgroundColor = '';
        mButton.style.backgroundColor = '';
        rButton.style.backgroundColor = 'rgb(239, 68, 68)'; 
    });
    fButton.addEventListener('click', function() {
        frequencyDiv.style.display = 'block';
        recencyDiv.style.display = 'none'; 
        monetaryDiv.style.display = 'none';
        rButton.style.backgroundColor = '';
        mButton.style.backgroundColor = '';
        fButton.style.backgroundColor = 'rgb(239, 68, 68)'; 
    });
    mButton.addEventListener('click', function() {
        monetaryDiv.style.display = 'block'; 
        recencyDiv.style.display = 'none';
        frequencyDiv.style.display = 'none';
        rButton.style.backgroundColor = '';
        fButton.style.backgroundColor = '';
        mButton.style.backgroundColor = 'rgb(239, 68, 68)'; 
    });
});