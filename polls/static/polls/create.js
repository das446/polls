
var lastid = 1;

function addChoice(){
    var list = document.getElementById('choices');
    var entry = document.createElement('li');
    var c=document.createElement("input");
    c.setAttribute('type','text');
    entry.appendChild(c);
    entry.setAttribute('name','choice'+lastid);
    entry.setAttribute('id','choice'+lastid);
    var removeButton = document.createElement('input');
    removeButton.setAttribute('type','button');
    removeButton.setAttribute('value','Remove');
    removeButton.setAttribute('onClick','removeChoice("'+'choice'+lastid+'")');
    entry.appendChild(removeButton);
    lastid+=1;
    list.appendChild(entry);
}

function removeChoice(itemid){
    console.log(itemid);
    var list = document.getElementById('choices');
    if(list.childElementCount==1){return;}
    var item = document.getElementById(itemid);
    console.log(item);
    list.removeChild(item);
}