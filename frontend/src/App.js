import "./App.css";
import Create from "./components/create";
import Read from "./components/read";
import Update from "./components/update";
import { Button } from "semantic-ui-react";
import { Link } from "react-router-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="main">
        <h2 className="main-header">Recommendation Operations</h2>
        <Link to="/read">
          <Button content='List' icon={{ color: '#212121', name: 'list' }} />
        </Link>
        <div>
          <Route exact path="/create" component={Create} />
        </div>
        <div style={{ marginTop: 20 }}>
          <Route exact path="/read" component={Read} />
        </div>

        <Route path="/update" component={Update} />
      </div>
    </Router>
  );
}

export default App;
