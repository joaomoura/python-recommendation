import axios from "axios";
import React, { useEffect, useState } from "react";
import { Table, Button, List } from "semantic-ui-react";
import { Link } from "react-router-dom";

export default function Read() {
  const [APIData, setAPIData] = useState([]);
  useEffect(() => {
    axios.get(`http://localhost:8000/recommendation`).then((response) => {
      const data = response.data["data"][0];
      setAPIData(data);
    });
  }, []);

  const setData = (data) => {
    let { id, name, knows } = data;
    localStorage.setItem("ID", id);
    localStorage.setItem("Name", name);
    localStorage.setItem("Knows", knows);
  };

  const getData = () => {
    axios.get(`http://localhost:8000/recommendation`).then((getData) => {
      const data = getData.data["data"][0];
      setAPIData(data);
    });
  };

  const onDelete = (id) => {
    axios.delete(`http://localhost:8000/recommendation/${id}`).then(() => {
      getData();
    });
  };

  return (
    <div>
      <div style={{ marginTop: 20 }}>
        <Link to="/create">
          <Button>New</Button>
        </Link>
      </div>
      <Table singleLine>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>ID-Name</Table.HeaderCell>
            <Table.HeaderCell>Knows</Table.HeaderCell>
            <Table.HeaderCell>Update</Table.HeaderCell>
            <Table.HeaderCell>Delete</Table.HeaderCell>
          </Table.Row>
        </Table.Header>

        <Table.Body>
          {APIData.map((data) => {
            return (
              <Table.Row>
                <Table.Cell>
                  <p style={{ textAlign: 'center' }}>{data.id}</p>
                  <p style={{ textAlign: 'center' }}>{data.name}</p>
                </Table.Cell>
                <Table.Cell>
                  <List>
                    {data.knows.map((know) => {
                      return <List.Item>{know}</List.Item>;
                    })}
                  </List>
                </Table.Cell>
                <Table.Cell>
                  <Link to="/update">
                    <Button onClick={() => setData(data)}>Update</Button>
                  </Link>
                </Table.Cell>
                <Table.Cell>
                  <Button onClick={() => onDelete(data.id)}>Delete</Button>
                </Table.Cell>
              </Table.Row>
            );
          })}
        </Table.Body>
      </Table>
    </div>
  );
}
