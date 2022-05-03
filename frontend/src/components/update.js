import React, { useState, useEffect } from "react";
import { Button, Form } from "semantic-ui-react";
import axios from "axios";
import { useHistory } from "react-router";

export default function Update() {
  let history = useHistory();
  const [id, setID] = useState(null);
  const [name, setName] = useState("");
  const [knows, setKnows] = useState("");

  useEffect(() => {
    setID(localStorage.getItem("ID"));
    setName(localStorage.getItem("Name"));
    setKnows(localStorage.getItem("Knows").split(','));
  }, []);

  const updateAPIData = e => {
    axios
      .put(`http://localhost:8000/recommendation/${id}`, {
        name,
        knows,
      })
      .then(() => {
        history.push("/read");
      });
  };

  return (
    <div>
      <Form className="create-form">
        <Form.Field>
          <label>Name</label>
          <input
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Field>
        <Form.Field>
          <label>Knows</label>
          <textarea
            placeholder="Knows"
            value={knows.toString().split(',')}
            onChange={(e) => {
              setKnows(e.target.value.split(","));
            }}
          />
        </Form.Field>
        <Button type="submit" onClick={updateAPIData}>
          Update
        </Button>
      </Form>
    </div>
  );
}
