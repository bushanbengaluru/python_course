apply css in each component
now go to First.js
 in <div className='firstcomp'>
# go to src create First.css
.First h1{
    color: blue;
}
#step 2: go to First.js
 import './First.css';
function First(){
    return (
     <div className="firstcomp">
       <h1> this first components</h1>
        </div>
    );
}
export default First;
# now second i want red
go to Second.js
<div className='secondcomp'>
# go to src -- create Second.css file
.secondcomp h1{
    color: red;
}
#step 2: go to Second.js
import './Second.css';
function Second(){
    return (
<div className='secondcomp'>
    <h1>this is my Second Component</h1>
</div>
    );
}
export default Second;

# now we can create one  by one with box
  go to First.css
  .firstcomp{
    height: 300px;
    width: 200px;
    border: 2px solid black;
}
  # and go to Second.css
  .secondcomp{
    height: 300px;
    width: 200px;
    border: 2px solid black;
}
  # now i want both box side by side
  #now go to App.css
  .App {
  text-align: center;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly; # two boxes spacess
}












