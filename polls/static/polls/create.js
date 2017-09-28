
var lastid = 1;

function addChoice(){
    let list = document.getElementById('choices');
    let entry = document.createElement('li');
    let c=document.createElement("input");
    c.setAttribute('type','text');
    c.setAttribute('name','choice'+lastid);
    entry.appendChild(c);
    entry.setAttribute('id','choice'+lastid);
    let removeButton = document.createElement('input');
    removeButton.setAttribute('type','button');
    removeButton.setAttribute('value','Remove');
    removeButton.setAttribute('onClick','removeChoice("'+'choice'+lastid+'")');
    entry.appendChild(removeButton);
    lastid+=1;
    list.appendChild(entry);
    let count=document.getElementById('choice_count');
    let countN=count.getAttribute('value');
    countN++;
    count.setAttribute('value',countN)

}

function removeChoice(itemid){
    let list = document.getElementById('choices');
    if(list.childElementCount==1){return;}
    let item = document.getElementById(itemid);
    list.removeChild(item);
    console.log(list.childElementCount);
    var choices= list.getElementsByTagName('li');
    for(let i=0;i<choices.length;i++){
        let choice = choices[i];
        console.log(choice);
        choice.setAttribute('id','choice'+i)
        choice.getElementsByTagName('input')[0].setAttribute('name','choice'+i);
        choice.getElementsByTagName('input')[1].setAttribute('onClick','removeChoice("'+'choice'+i+'")');
    }

    let count=document.getElementById('choice_count');
    let countN=count.getAttribute('value');
    countN--;
    count.setAttribute('value',countN)
}