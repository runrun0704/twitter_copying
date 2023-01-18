import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';
import {baseURL} from './baseURL';

function ApiGet() {
    const [tweet,setTweet] = useState([])

    useEffect(() => {
        axios.get(`${baseURL}tweets`)
        .then(res => {
            setTweet(res.data)
        })
    }, [])

    return(
        <div>
            <h2>Api_get</h2>
            <div>
                {tweet.map(item => (
                    <div>
                        <Link
                            to={`/pdca/${item.id}`}
                            key={item.id}
                        >
                            {item.title}
                        </Link>
                        <p>{item.body}</p>
                        <p>{item.user_id}</p>
                        <p>{item.good_count}</p>
                        <h3>〆</h3>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default ApiGet;
