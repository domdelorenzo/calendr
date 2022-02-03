import Client from './api';

export const CreateUser = async (username) => {
  const res = await Client.post('/users/', { username });
  return res.data;
};

export const FindUsername = async (username) => {
  const res = await Client.get(`/users/search?username=${username}`);
  return res.data;
};
