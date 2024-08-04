(function kakuninInput() {
    'use strict';

    const numberCard = new Map([
        ['A-1', '01'],
        ['A-2', '02'],
        ['A-3', '03'],
        ['A-4', '04'],
        ['A-5', '05'],
        ['B-1', '06'],
        ['B-2', '07'],
        ['B-3', '08'],
        ['B-4', '09'],
        ['B-5', '10'],
        ['C-1', '11'],
        ['C-2', '12'],
        ['C-3', '13'],
        ['C-4', '14'],
        ['C-5', '15'],
        ['D-1', '16'],
        ['D-2', '17'],
        ['D-3', '18'],
        ['D-4', '19'],
        ['D-5', '20'],
        ['E-1', '21'],
        ['E-2', '22'],
        ['E-3', '23'],
        ['E-4', '24'],
        ['E-5', '25'],
    ]);

    const replaceFullToHalf = str => str.replace(/[！-～]/g, s => String.fromCharCode(s.charCodeAt(0) - 0xFEE0));
    const kakuninNumbers = Array.from(document.querySelectorAll('span.kakunin-no-label nobr')).map(el => replaceFullToHalf(el.innerText));
    const inputElements = Array.from(document.querySelectorAll('input.kakunin-no-field'));
    if (inputElements.length !== kakuninNumbers.length) {
        console.error('要素数と確認番号の数が一致しません');
        return;
    }
    for (const [index, inputElement] of inputElements.entries()) {
        console.log(`${kakuninNumbers[index]} => ${numberCard.get(kakuninNumbers[index])}`);
        inputElement.value = numberCard.get(kakuninNumbers[index]);
    }
})();