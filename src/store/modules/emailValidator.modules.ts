export type State = {
  email: string;
  emails: string [];
}

const state: State = {
  email: "",
  emails: []
}


const getters = {
  currentEmail (state: any) {
      return state.email
  },
  currentEmailss (state: any) {
      return state.emails
  }
}

const actions = {
  async validateEmail (context: any) {
    const email = context.rootGetters.email;
    const response = await fetch(`https://www.disify.com/api/email/${email}`);
    const responseData = await response.json();

    if (!response.ok) {
      const error = new Error(responseData.message || 'Failed to fetch requests.');
      throw error;
    }
    const requests = [];

    for (const key in responseData) {
      const request: unknown = {
        format: responseData[key].format,
        domain: responseData[key].domain, 
        disposable: responseData[key].userEmail,
        dns: responseData[key].message,
        whitelist:responseData[key].whitelist
      };
      requests.push(request);
    }

    context.commit('setRequests', requests);
  }
}

const mutations = {
  setEmails (state: any, Emails: any) {
      state.Emails = Emails
  },
  setEmail (state: any, Email: any) {
      state.Email = Email
  }
}


export default {
  state,
  actions,
  mutations,
  getters
}