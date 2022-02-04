import Client from './api';

export const CreateUser = async (username) => {
  const res = await Client.post('/users/', { username });
  return res.data;
};

export const FindUsername = async (username) => {
  const res = await Client.get(`/username/${username}`);
  return res.data;
};

export const GetUser = async (id) => {
  const res = await Client.get(`/users/${id}`);
  return res.data
}

export const PostEvent = async (event) => {
  const res = await Client.post(`/events/`, event)
  return res.data
}

export const DeleteEvent = async (id) => {
  const res = await Client.delete(`/events/${id}`)
  return res.data;
}