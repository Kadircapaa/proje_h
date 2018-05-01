import React, { Component } from 'react';
import './App.css';


export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      term: '',
      items: [],
     
    };
  }

  componentDidMount() {
    fetch(`http://127.0.0.1:8000/api/User/`, {
        method: 'GET',
        headers: {
          'content-type': 'application/json',
        }
      })
      .then((res) => res.json())
      .then(res => console.log(res)).then(
    fetch('http://127.0.0.1:8000/api/User/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        //baslangıcta auto user olusturmak ıcın bu commentler acılabilir.
        //list:{   //list kullanılınca hata alıyor. listsiz kullanılmalı
          //user: 'testuser0',
          //password: 'testpasswor0',
          //email: 'email2@email0.com'
       // }
      })
    }))
    .then((res) => res.json())
    .then(res => console.log(res))
    .then(( data ) => {
      this.setState({
        listId: data.list.id,
        listUserName:data.list.user,
        listPassword:data.list.password,
        listEmail:data.list.email,
      });
    });
  }

  onChange = (event) => {
    this.setState({ term: event.target.value });
  }  

  onSubmit = (event) => {
    event.preventDefault();
    const { listId,term } = this.state;

    fetch('http://127.0.0.1:8000/api/User/', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify({
        //list: {
          id: listId,
          user: term,  //hepsine arayuzden alınan deger verildi.
          password:term,  //hepsine arayuzden alınan deger verildi.
          email: term //hepsine arayuzden alınan deger verildi.
       // }
      })
    })
    .then(() => {
      return fetch(`http://127.0.0.1:8000/api/User/${listId}`, {
        method: 'GET',
        headers: {
          'content-type': 'application/json',
        }
      })
      .then((res) => res.json())
      .then(res => console.log(res))
    })
    .then((data) => {
      this.setState({
     user: data.list.items.map(({ user }) => user)
      })
    });
  }

  render() {
    return (
      <div>
        <form className="App" onSubmit={this.onSubmit}>
          <h2>Please Add Items For List</h2>
          <input value={this.state.term} onChange={this.onChange} />
          <button>Submit</button>
        </form>

      </div>
    );
  }
}