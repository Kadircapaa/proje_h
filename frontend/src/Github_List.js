import React, { Component } from 'react';

const urlForUsername = todolist_owner_id =>

  `http://127.0.0.1:8000/api/Lists/${todolist_owner_id}/?format=json`


class GitHub extends Component {
  constructor(props) {
    super(props)
    this.state = {
      requestFailed: false
    }
  }

  componentDidMount() {
    fetch(urlForUsername(this.props.todolist_owner_id))
      .then(response => {
        if (!response.ok) {
          throw Error("Network request failed")
        }

        return response
      })
      .then(d => d.json())
      .then(d => {
        this.setState({
          githubData: d
        })
      }, () => {
        this.setState({
          requestFailed: true
        })
      })
  }

  render() {

    if (this.state.requestFailed) return <p>Failed!</p>
    if (!this.state.githubData) return <p>Loading...</p>
    return (
      <div>
        <h2>{this.state.githubData.todolist_owner_id}</h2>
        <h2>{this.state.githubData.todolist_name}</h2>
        <h2>{this.state.githubData.todolist_due_date}</h2>
        <h2>{this.state.githubData.todolist_status}</h2>
      </div>
    )
  }
}



export default GitHub;


