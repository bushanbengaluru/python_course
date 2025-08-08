# life cycle stages of the react js
# we have three stages
  # exm we can take component -- like
  # we have a exm Show/Hide -- first we can click
  # the button first we can go to main compoment
  # mount
1 Mount
the button first we can go to main compoment
  # mount
2 update : can case we changes any in that is update

3 unmount : again we can click button that is unmount
# now go to Main.js
function Main(){
    let [show,setshow]=useState(false)
    return(
        <div className="maincomp">
          <button onClick={()=>setshow(!show)}>Show/Hide</button>

      {show? <ShowHide/>:''}
        </div>

    );
}
export default Main;
# and run the code then go to inspect then see the html code
and click the Show/Hide button autometically we can get html code that is mounting
and now again click the Show/Hide button owr code remove that is unmounting

# update: now go to Show/Hide.js create one text files
import { useState } from "react";
function ShowHode()
{
    let [data,setData]=useState('');
    return(
        <div>
            <h1>We are good student</h1>
            <input type="text" onChange={(event)=>setData(event.target.value)}/>
            <p>{data}</p>
        </div>
    )
}
export default ShowHode;
# now run the project and click button then see we can update and mount and unmount
at a time
# now why we need this means there is a  hook called useEffect
useEffect: will be acting acoding to the life cycle method
useEffect takes two input 1 function 2 dependency array

# now go to Show/Hide.js file
# 
function ShowHode()
{
    let [data,setData]=useState('');
    useEffect(
        ()=>{
        console.log('Component mounted');
    }
);# this code is function based : owr print data will print multiple time

# 2 dependency array : once we call this we did't print multiple time
    # but we can get two times for console.log(component) why bcz react js will
    #    check print and testing 
    function ShowHode()
{
    let [data,setData]=useState('');
    useEffect(
        ()=>{
        console.log('Component mounted');
    },[]
);

# now i wanr unmounted in useEffect
# now go to Show/Hide.js file

function ShowHode()
{
    let [data,setData]=useState('');
    useEffect(
        ()=>{
        console.log('Component mounted');
        return()=>{ #once we call return unmounted will call
            console.log('component unmounted');
        }
    },[]
);
# now we can print 'Component mounted' two times in case i dont want to two time
    # now go to index.js and comment it then run and see we can get one time
   // <React.StrictMode>
    <App />
//</React.StrictMode>

    # we get data in API's so how to do


