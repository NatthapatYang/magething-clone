document.addEventListener('DOMContentLoaded', function() {
    const segmentBtns = document.querySelectorAll('#rfm-buttons button');
    const barChartElem = document.querySelectorAll('.bar-chart');

    setDefaultSegment();

    segmentBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const segmentType = this.dataset.segmentType

            removeHighlightFromAllButtons();
            highlightSelectedSegment(this);

            handleActiveSegment(segmentType);
        });
    })

    function setDefaultSegment() {
        const defaultSegment = 'recency';
        const defaultSegmentElem = document.getElementById(defaultSegment);

        highlightSelectedSegment(segmentBtns[0])
        showSelectedSegment(defaultSegmentElem);
    }

    function handleActiveSegment(segmentType) {
        const segmentElem = document.getElementById(segmentType);

        hideAllSegments();
        showSelectedSegment(segmentElem);
    }

    function hideAllSegments() {
        barChartElem.forEach((elem) => {
            elem.style.display = 'none';
        });
    }

    function showSelectedSegment(segmentElem) {
        segmentElem.style.display = 'block';
    }

    function removeHighlightFromAllButtons() {
        segmentBtns.forEach((btn) => {
            btn.style.backgroundColor = '';
        });
    }

    function highlightSelectedSegment(btn) {
        btn.style.backgroundColor = 'rgb(239, 68, 68)';
    }
});