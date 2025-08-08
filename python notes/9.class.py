# one projectos  To Do list:
1 create ToDo component in that im taking emty list
  like x=[]
# now create ToDoList.js
function ToDoList(){
    return(
        <div className="todocomp">
        <input type="text" />
        <button>Add</button>
        </div> 
    )
}
export default ToDoList;
# now go to Main.js
import ToDoList from "./ToDoList";
function Main(){ 
    return(
        <div className="maincomp">
      <ToDoList />
        </div>
    );
}
export default Main;

# now go to ToDoList.js
function ToDoList(){
    let item='';
    let todolist=[];
    let additem=()=>{
        todolist.push(item);
        console.log(todolist)
    }
    return(
        <div className="todocomp">
        <input type="text" onChange={(event)=>item=event.target.value}/>
        <button onClick={additem}>Add</button>
        {todolist.map((it)=>{
            return <p>{it}</p>
        })}
        </div> 
    )
}
export default ToDoList;

# now import useState bcz re-render
import { useState } from "react";
function ToDoList(){
    let item='';
    let [todolist,setToList]=useState([]) # useState takes empy list
    let additem=()=>{
        #todolist.push(item);
          setToList([...todolist,item]) #... is unpacking operators
           #x=[1,2,3]
          # x=[*x,4]
          # print(x)-- 1,2,3,4
           # ...todolist(it is spread operator) use to already existing value with new
                #    value 
        console.log(todolist)
    }
    return(
        <div className="todocomp">
        <input type="text" onChange={(event)=>item=event.target.value}/>
        <button onClick={additem}>Add</button>
        {todolist.map((it)=>{
            return <p>{it}</p>
        })}
        </div> 
    )
}
export default ToDoList;
# we can write this
 return <p>{it}</p> <button>X</button> get syntax error
#now we can call fragment
# fragment :  combine multiple tags into a single unit
 #now in ToDoList.js
# <></> this is fragment tags
{todolist.map((it)=>{
            return <><p>{it}</p> <button>X</button></>
        })}
# now we can get the X button bellow now change the css
# now go to ToDoList.js
# and im given specail id to this add button 
 <button className='btm' onClick={additem}>Add</button>
 # and now goto Main.css
   maincomp .btn{
    height: 70px;
    width: 120px;
    margin-top: 40px;
    background-color: blue;
    color: white;
    font-size: x-large;
    border: none;
    margin: 20px;
}
   .maincomp p{
    display: inline;
}
# and now go to ToDoList.js we can give the <br/><br/>
<button className='btm' onClick={additem}>Add</button><br/><br/>
# now we want space value with  X
# now go to Main.css
    .maincomp p{
    #display: inline;
    margin-right: 20px;
}
# now can add the value we got side side now we want line by libe
# go to ToDoList give the <br/>
 return <><p>{it}</p> <button>X</button><br/><br/></>
# now you can click X remove the particuler item
now go to ToDoList.js
let removeitem=(idx)=>{
        let output;
        output=todolist.filter((it,index)=>{
 # filter is function we can get exatly values and give the value in index
      return index!=idx;
        });
        setToList(output)
    }
    return(
        <div className="todocomp">
        <input type="text" onChange={(event)=>item=event.target.value}/>
        <button className='btm' onClick={additem}>Add</button><br/><br/>
        {todolist.map((it,idx)=>{
  return <><p>{it}</p> <button onClick={()=>removeitem(idx)}>X</button><br/><br/></>
    # idx mean we can delete particulet index so we can cal idx
        })}
        </div> 
    )
}
export default ToDoList;






   
 


