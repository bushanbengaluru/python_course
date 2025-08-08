create component
Second.js in src

function Second(){
    return (
<div>
    <h1>this is my Second Component</h1>
</div>
    );
}
export default Second;

# then go to App.js
import Second from './Second';
function App() {
  return (
    <div className="App">
      <h1>this is my first react project</h1>
      <First />
      <Second />
    </div>
  );
