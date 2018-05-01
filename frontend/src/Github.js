import React, { Component } from 'react';



const urlForUsername = username =>
//`http://127.0.0.1:8000/api/KullaniciGosterme//?format=json`
  `http://127.0.0.1:8000/api/User/${username}/?format=json`

const urlForList = username =>
//`http://127.0.0.1:8000/api/KullaniciGosterme//?format=json`
  `http://127.0.0.1:8000/api/Lists/${username}/?format=json`


const urlForItem = username =>
//`http://127.0.0.1:8000/api/KullaniciGosterme//?format=json`
  `http://127.0.0.1:8000/api/Items//${username}/?format=json`



class GitHub extends Component {
  constructor(props) {
    super(props)
    this.state = {
      requestFailed: false
    }
  }

  componentDidMount() {
    fetch(urlForUsername(this.props.username))
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
         <h2>
            { this.props.username ?  'You are logged In' : 'You are not logged In' }
          </h2>
        <h2>{this.state.githubData.id}</h2>
        <h2>{this.state.githubData.user}</h2>
        <h2>{this.state.githubData.password}</h2>
        <h2>{this.state.githubData.email}</h2>
        <h2>{this.state.githubData.create_date}</h2>
        <h2>{this.state.githubData.edited_date}</h2>
      </div>
    )
  }
}

export default GitHub;


