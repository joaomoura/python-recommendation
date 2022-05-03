import React, { useState, useEffect } from "react";
import { Button, Form } from "semantic-ui-react";
import axios from "axios";
import { useHistory } from "react-router";

export default function Create() {
  let history = useHistory();
  const [name, setName] = useState("");
  const [knows, setKnows] = useState("");

  useEffect(() => {
    setKnows([]);
  }, []);

  const postData = () => {
    axios
      .post(`http://localhost:8000/recommendation`, {
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
            onChange={(e) => setName(e.target.value)}
          />
        </Form.Field>
        <Form.Field>
          <label>Knows</label>
          <textarea
            placeholder="Knows"
            onChange={(e) => {
              setKnows(e.target.value.split(","));
            }}
          />
        </Form.Field>
        <Button onClick={postData} type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
}
