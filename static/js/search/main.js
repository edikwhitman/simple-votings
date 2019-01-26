function get_ref()
  {
    let q = search_question.value
    let auth = search_user.value

    search_submit.href = '/search_vote/?'

    if (q.length > 0)
      search_submit.href += 'q=' + q + '&'
    if (auth.length > 0)
      search_submit.href += 'author=' + auth
  }