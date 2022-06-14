// script 
// task 1
console.log("hello")


var checkb = document.querySelectorAll('.checkbox1');



sum1 = 0;
sum2 = 0;
checkb.forEach((check, index) => {
    check.addEventListener('click', function () {

        if (this.checked == true) {

            var table = document.getElementById("table1");
            sum1 = sum1 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum2 = sum2 + parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table1");
            sum1 = sum1 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum2 = sum2 - parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else {
            sum1 = 0;
            sum2 = 0;
            document.getElementById('selected').innerHTML = sumval;
        }
    })
})


var checkb = document.querySelectorAll('.checkbox2');
console.log(checkb)


sum3 = 0;
sum4 = 0;
checkb.forEach((check, index) => {
    check.addEventListener('click', function () {
        if (this.checked == true) {

            var table = document.getElementById("table2");
            sum3 = sum3 + parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum4 = sum4 + parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else if (this.checked != true) {
            var table = document.getElementById("table2");
            sum3 = sum3 - parseInt(table.rows[index + 1].cells[2].innerHTML);
            sum4 = sum4 - parseInt(table.rows[index + 1].cells[1].innerHTML);
            first()
        }
        else {
            sum2 = 0;
            document.getElementById('selected').innerHTML = sum2;
        }
    })
})

function first() {
    debit = sum1 - sum3;
    credit = sum2 - sum4
    document.getElementById('selected').innerHTML = debit;
    document.getElementById('selected2').innerHTML = credit;
}

// end task 1


// task 2 
count = 0;
const count_list = []
function newRow() {
    a = count++;
    count_list.push(a);
    DEBIT = document.createElement('input');
    DEBIT.setAttribute("type", 'text');
    DEBIT.setAttribute("class", 'text');
    DEBIT.setAttribute("id", +count + 'debit');
    DEBIT.setAttribute("onkeypress", 'myFunction1(event)');


    CREDIT = document.createElement('input');
    CREDIT.setAttribute("type", 'text');
    CREDIT.setAttribute("id", +count + 'credit');
    CREDIT.setAttribute("onkeypress", 'myFunction2(event)');


    var slect = document.getElementById("add-row");
    option = slect.options[slect.selectedIndex].value;

    var tbodyRef = document.getElementById('table3');

    // Insert a row at the end of table
    var newRow = tbodyRef.insertRow(1);

    // Insert a cell at the end of the row
    var newCell = newRow.insertCell(0);
    var newCell1 = newRow.insertCell(1).appendChild(DEBIT);
    var newCell2 = newRow.insertCell(2).appendChild(CREDIT);
    var newCell3 = newRow.insertCell(3);
    var newCell4 = newRow.insertCell(4);

    newCell.innerHTML = option;

}