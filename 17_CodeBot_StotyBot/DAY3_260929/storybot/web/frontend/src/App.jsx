import { useEffect, useRef, useState } from 'react'
import { api, jsonOptions } from './api'

const dateText = (value) => value ? new Date(`${value.replace(' ', 'T')}Z`).toLocaleDateString('ko-KR', { year: 'numeric', month: 'long', day: 'numeric' }) : ''

function StoryCard({ story, onOpen, onLike, user }) {
  const preview = story.body.length > 180 ? `${story.body.slice(0, 180).trim()}…` : story.body
  return (
    <article className="story-card">
      <div className="card-topline"><span className="card-ornament">✦</span><span>{dateText(story.created_at)}</span></div>
      <button className="card-content" onClick={() => onOpen(story)} aria-label={`${story.title} 읽기`}>
        <h3>{story.title}</h3>
        <p>{preview}</p>
      </button>
      <div className="card-footer">
        <span className="author"><span className="author-avatar">{story.author_nickname.slice(0, 1)}</span>{story.author_nickname}</span>
        <div className="card-actions">
          {!story.is_public && <span className="private-label">비공개</span>}
          {story.is_public && <button className={`heart-button ${story.liked_by_me ? 'is-liked' : ''}`} onClick={() => onLike(story)} aria-label={story.liked_by_me ? '좋아요 취소' : '좋아요'} title={!user ? '로그인 후 좋아요를 누를 수 있어요' : ''}><span>{story.liked_by_me ? '♥' : '♡'}</span> {story.like_count}</button>}
        </div>
      </div>
    </article>
  )
}

function AuthDialog({ onClose, onSuccess }) {
  const [mode, setMode] = useState('login')
  const [email, setEmail] = useState('')
  const [nickname, setNickname] = useState('')
  const [password, setPassword] = useState('')
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  async function submit(event) {
    event.preventDefault()
    setError('')
    setBusy(true)
    try {
      const body = mode === 'register' ? { email, nickname, password } : { email, password }
      const person = await api(`/auth/${mode}`, jsonOptions('POST', body))
      onSuccess(person)
    } catch (problem) {
      setError(problem.message)
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="modal-backdrop" onMouseDown={onClose}>
      <section className="modal auth-modal" role="dialog" aria-modal="true" aria-labelledby="auth-title" onMouseDown={(event) => event.stopPropagation()}>
        <button className="modal-close" onClick={onClose} aria-label="닫기">×</button>
        <div className="eyebrow">YOUR NEXT CHAPTER</div>
        <h2 id="auth-title">{mode === 'login' ? '다시 만나 반가워요' : '이야기의 주인공이 되어보세요'}</h2>
        <p className="subtle">{mode === 'login' ? '로그인하고 새로운 이야기를 이어가세요.' : '몇 가지만 적으면 당신의 이야기가 시작돼요.'}</p>
        <form onSubmit={submit} className="form-stack">
          <label>이메일<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required autoComplete="email" placeholder="you@example.com" /></label>
          {mode === 'register' && <label>닉네임<input value={nickname} onChange={(event) => setNickname(event.target.value)} required minLength={2} maxLength={30} placeholder="이야기꾼" /></label>}
          <label>비밀번호<input type="password" value={password} onChange={(event) => setPassword(event.target.value)} required minLength={mode === 'register' ? 8 : undefined} autoComplete={mode === 'register' ? 'new-password' : 'current-password'} placeholder="비밀번호 입력" /></label>
          {error && <p className="form-error" role="alert">{error}</p>}
          <button className="button button-primary full" disabled={busy}>{busy ? '잠시만요…' : mode === 'login' ? '로그인' : '회원가입'}</button>
        </form>
        <p className="switch-auth">{mode === 'login' ? '아직 계정이 없나요?' : '이미 계정이 있나요?'} <button onClick={() => { setMode(mode === 'login' ? 'register' : 'login'); setError('') }}>{mode === 'login' ? '회원가입' : '로그인'}</button></p>
      </section>
    </div>
  )
}

function StoryDialog({ story, user, onClose, onLike, onUpdated, onDeleted }) {
  const [editing, setEditing] = useState(false)
  const [title, setTitle] = useState(story.title)
  const [body, setBody] = useState(story.body)
  const [isPublic, setIsPublic] = useState(story.is_public)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const mine = user?.id === story.author_id

  async function save(event) {
    event.preventDefault()
    setBusy(true)
    setError('')
    try {
      const changed = await api(`/stories/${story.id}`, jsonOptions('PATCH', { title, body, is_public: isPublic }))
      onUpdated(changed)
      setTitle(changed.title)
      setBody(changed.body)
      setIsPublic(changed.is_public)
      setEditing(false)
    } catch (problem) {
      setError(problem.message)
    } finally {
      setBusy(false)
    }
  }

  async function remove() {
    if (!window.confirm('이 스토리를 영구 삭제할까요?')) return
    setBusy(true)
    setError('')
    try {
      await api(`/stories/${story.id}`, { method: 'DELETE' })
      onDeleted(story.id)
    } catch (problem) {
      setError(problem.message)
      setBusy(false)
    }
  }

  return (
    <div className="modal-backdrop" onMouseDown={onClose}>
      <section className="modal story-modal" role="dialog" aria-modal="true" aria-labelledby="story-title" onMouseDown={(event) => event.stopPropagation()}>
        <button className="modal-close" onClick={onClose} aria-label="닫기">×</button>
        <div className="eyebrow">A STORY TO REMEMBER</div>
        {editing ? (
          <form onSubmit={save} className="form-stack editor-form">
            <label>제목<input value={title} onChange={(event) => setTitle(event.target.value)} required maxLength={120} /></label>
            <label>이야기<textarea value={body} onChange={(event) => setBody(event.target.value)} rows={13} required maxLength={20000} /></label>
            <label>공개 여부<select value={isPublic ? 'public' : 'private'} onChange={(event) => setIsPublic(event.target.value === 'public')}><option value="public">공개</option><option value="private">비공개</option></select></label>
            {error && <p className="form-error" role="alert">{error}</p>}
            <div className="dialog-actions"><button type="button" className="button button-quiet" onClick={() => setEditing(false)}>취소</button><button className="button button-primary" disabled={busy}>{busy ? '저장 중…' : '변경 저장'}</button></div>
          </form>
        ) : (
          <>
            <h2 id="story-title">{story.title}</h2>
            <div className="story-meta"><span>by {story.author_nickname}</span><span>·</span><span>{dateText(story.created_at)}</span>{!story.is_public && <span className="private-label">비공개</span>}</div>
            <div className="story-body">{story.body}</div>
            {error && <p className="form-error" role="alert">{error}</p>}
            <div className="dialog-actions">
              {story.is_public && <button className={`heart-button large ${story.liked_by_me ? 'is-liked' : ''}`} onClick={() => onLike(story)}><span>{story.liked_by_me ? '♥' : '♡'}</span> 좋아요 {story.like_count}</button>}
              {mine && <div className="owner-actions"><button className="text-button" onClick={() => setEditing(true)}>수정</button><button className="text-button danger" onClick={remove} disabled={busy}>삭제</button></div>}
            </div>
          </>
        )}
      </section>
    </div>
  )
}

function AccountView({ user, onUpdate, onLoggedOut }) {
  const [email, setEmail] = useState(user.email)
  const [nickname, setNickname] = useState(user.nickname)
  const [profilePassword, setProfilePassword] = useState('')
  const [oldPassword, setOldPassword] = useState('')
  const [newPassword, setNewPassword] = useState('')
  const [deletePassword, setDeletePassword] = useState('')
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const [busy, setBusy] = useState(false)

  async function updateProfile(event) {
    event.preventDefault()
    setBusy(true); setError(''); setMessage('')
    try {
      const person = await api('/auth/me', jsonOptions('PATCH', { email, nickname, current_password: profilePassword || null }))
      onUpdate(person)
      setProfilePassword('')
      setMessage('회원정보를 변경했습니다.')
    } catch (problem) { setError(problem.message) } finally { setBusy(false) }
  }

  async function changePassword(event) {
    event.preventDefault()
    setBusy(true); setError(''); setMessage('')
    try {
      await api('/auth/password', jsonOptions('PATCH', { current_password: oldPassword, new_password: newPassword }))
      onLoggedOut('비밀번호가 변경되었습니다. 다시 로그인해 주세요.')
    } catch (problem) { setError(problem.message) } finally { setBusy(false) }
  }

  async function deleteAccount(event) {
    event.preventDefault()
    if (!window.confirm('계정과 모든 스토리·좋아요를 영구 삭제할까요?')) return
    setBusy(true); setError(''); setMessage('')
    try {
      await api('/auth/me', jsonOptions('DELETE', { current_password: deletePassword }))
      onLoggedOut('계정과 스토리가 삭제되었습니다.')
    } catch (problem) { setError(problem.message) } finally { setBusy(false) }
  }

  return (
    <section className="page-section account-page">
      <div className="section-heading"><div><div className="eyebrow">MY ACCOUNT</div><h1>내 계정</h1><p>당신의 이야기를 담는 공간을 관리하세요.</p></div></div>
      {message && <p className="notice success" role="status">{message}</p>}
      {error && <p className="notice error" role="alert">{error}</p>}
      <div className="account-grid">
        <div className="account-panel"><span className="panel-index">01 / PROFILE</span><h2>회원정보</h2><form onSubmit={updateProfile} className="form-stack"><label>닉네임<input value={nickname} onChange={(event) => setNickname(event.target.value)} required minLength={2} maxLength={30} /></label><label>이메일<input type="email" value={email} onChange={(event) => setEmail(event.target.value)} required /></label><label>현재 비밀번호 <small>이메일을 바꿀 때 필요해요</small><input type="password" value={profilePassword} onChange={(event) => setProfilePassword(event.target.value)} autoComplete="current-password" /></label><button className="button button-primary" disabled={busy}>정보 저장</button></form></div>
        <div className="account-panel"><span className="panel-index">02 / PASSWORD</span><h2>비밀번호 변경</h2><form onSubmit={changePassword} className="form-stack"><label>현재 비밀번호<input type="password" value={oldPassword} onChange={(event) => setOldPassword(event.target.value)} required autoComplete="current-password" /></label><label>새 비밀번호<input type="password" value={newPassword} onChange={(event) => setNewPassword(event.target.value)} required minLength={8} autoComplete="new-password" /></label><button className="button button-outline" disabled={busy}>비밀번호 변경</button></form><p className="panel-note">변경 후 모든 로그인 세션이 종료됩니다.</p></div>
        <div className="account-panel danger-panel"><span className="panel-index">03 / GOODBYE</span><h2>회원 탈퇴</h2><p>계정과 작성한 스토리, 좋아요 기록이 모두 삭제됩니다.</p><form onSubmit={deleteAccount} className="form-stack"><label>현재 비밀번호<input type="password" value={deletePassword} onChange={(event) => setDeletePassword(event.target.value)} required autoComplete="current-password" /></label><button className="button button-danger" disabled={busy}>계정 삭제</button></form></div>
      </div>
    </section>
  )
}

export default function App() {
  const [section, setSection] = useState('home')
  const [user, setUser] = useState(null)
  const [publicStories, setPublicStories] = useState([])
  const [myStories, setMyStories] = useState([])
  const [selectedStory, setSelectedStory] = useState(null)
  const [showAuth, setShowAuth] = useState(false)
  const [prompt, setPrompt] = useState('')
  const [visibility, setVisibility] = useState('')
  const [generated, setGenerated] = useState(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [notice, setNotice] = useState('')
  const accountVersion = useRef(0)

  function switchAccount(person) {
    accountVersion.current += 1
    setUser(person)
    setMyStories([])
    setSelectedStory(null)
    setPrompt('')
    setVisibility('')
    setGenerated(null)
    setBusy(false)
    setError('')
  }

  async function refreshStories(currentUser = user, version = accountVersion.current) {
    try {
      const published = await api('/stories')
      if (version !== accountVersion.current) return
      setPublicStories(published)
      if (currentUser) {
        const mine = await api('/stories/mine')
        if (version !== accountVersion.current) return
        setMyStories(mine)
      }
      else setMyStories([])
    } catch (problem) { if (version === accountVersion.current) setError(problem.message) }
  }

  useEffect(() => {
    async function start() {
      const version = accountVersion.current
      let person = null
      try {
        person = await api('/auth/me')
        if (version !== accountVersion.current) return
        setUser(person)
      } catch { /* Anonymous visitor. */ }
      if (version === accountVersion.current) await refreshStories(person, version)
    }
    start()
  }, [])

  function navigate(next) {
    if (['write', 'mine', 'account'].includes(next) && !user) { setShowAuth(true); return }
    setSection(next); setError(''); setNotice(''); window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  async function logout() {
    try { await api('/auth/logout', { method: 'POST' }) } catch (problem) { setError(problem.message); return }
    switchAccount(null); setSection('home'); setNotice('로그아웃했습니다.'); await refreshStories(null)
  }

  function loggedOut(message) {
    switchAccount(null); setSection('home'); setNotice(message); refreshStories(null)
  }

  async function toggleLike(story) {
    if (!user) { setSelectedStory(null); setShowAuth(true); return }
    const version = accountVersion.current
    try {
      const changed = await api(`/stories/${story.id}/like`, { method: 'POST' })
      if (version !== accountVersion.current) return
      setSelectedStory((current) => current?.id === changed.id ? changed : current)
      setGenerated((current) => current?.id === changed.id ? changed : current)
      await refreshStories(user, version)
    } catch (problem) { if (version === accountVersion.current) setError(problem.message) }
  }

  async function generateStory(event) {
    event.preventDefault()
    if (!visibility) { setError('공개 여부를 선택해 주세요.'); return }
    const version = accountVersion.current
    setBusy(true); setError(''); setGenerated(null)
    try {
      const story = await api('/stories', jsonOptions('POST', { prompt, is_public: visibility === 'public' }))
      if (version !== accountVersion.current) return
      setGenerated(story)
      await refreshStories(user, version)
    } catch (problem) { if (version === accountVersion.current) setError(problem.message) }
    finally { if (version === accountVersion.current) setBusy(false) }
  }

  async function updatedStory(story, version) {
    if (version !== accountVersion.current) return
    setSelectedStory(story)
    setGenerated((current) => current?.id === story.id ? story : current)
    await refreshStories(user, version)
  }

  async function deletedStory(id, version) {
    if (version !== accountVersion.current) return
    setSelectedStory(null)
    setGenerated((current) => current?.id === id ? null : current)
    await refreshStories(user, version)
  }

  const renderedVersion = accountVersion.current

  return (
    <div className="app-shell">
      <header className="site-header"><div className="header-inner"><button className="brand" onClick={() => navigate('home')}><span className="brand-symbol">✦</span><span>Story<span>Bot</span><small>WHERE STORIES BEGIN</small></span></button><nav aria-label="주 메뉴"><button className={section === 'home' ? 'active' : ''} onClick={() => navigate('home')}>공개 이야기</button><button className={section === 'mine' ? 'active' : ''} onClick={() => navigate('mine')}>내 이야기</button><button className={section === 'write' ? 'active' : ''} onClick={() => navigate('write')}>이야기 쓰기</button></nav><div className="header-user">{user ? <><button className="nickname-button" onClick={() => navigate('account')}>{user.nickname} 님</button><button className="button button-small button-outline" onClick={logout}>로그아웃</button></> : <button className="button button-small button-primary" onClick={() => setShowAuth(true)}>로그인 / 가입</button>}</div></div></header>
      <main>
        {notice && <div className="top-notice" role="status">{notice}<button onClick={() => setNotice('')} aria-label="알림 닫기">×</button></div>}
        {section === 'home' && <>
          <section className="hero"><div className="hero-inner"><div className="hero-copy"><div className="eyebrow"><span className="eyebrow-line" />A PLACE FOR LITTLE WONDERS</div><h1>한 문장으로 시작하는<br /><em>나만의 이야기</em></h1><p>짧은 첫 문장을 건네주세요. 스토리봇이 다음 장면을 써 내려갑니다. 마음에 남는 이야기는 이곳에 간직하고 함께 나눠요.</p><div className="hero-actions"><button className="button button-primary button-large" onClick={() => navigate('write')}>이야기 시작하기 <span>↗</span></button><button className="hero-link" onClick={() => document.getElementById('story-library')?.scrollIntoView({ behavior: 'smooth' })}>다른 이야기 둘러보기 <span>↓</span></button></div><div className="hero-bottom"><span>✧ 한 줄에서 시작되는 무한한 상상</span><span>✧ 영어 동화 이어쓰기</span></div></div><div className="hero-art" aria-hidden="true"><div className="sun-disc" /><span className="sparkle sparkle-one">✦</span><span className="sparkle sparkle-two">✧</span><span className="sparkle sparkle-three">✦</span><div className="art-caption">Once upon a time...</div><div className="book-cover"><div className="book-inner"><span>THE<br />STORY<br />BEGINS</span><i>✧</i></div></div><div className="book-shadow" /></div></div></section>
          <section id="story-library" className="page-section library-section"><div className="section-heading"><div><div className="eyebrow">FROM OUR LIBRARY</div><h2>오늘의 이야기들</h2><p>누군가의 첫 문장에서 피어난 이야기를 만나보세요.</p></div><span className="heading-decoration">✧</span></div>{publicStories.length ? <div className="story-grid">{publicStories.map((story) => <StoryCard key={story.id} story={story} user={user} onOpen={setSelectedStory} onLike={toggleLike} />)}</div> : <div className="empty-state"><span>✦</span><h3>아직 첫 이야기를 기다리고 있어요</h3><p>첫 번째 이야기를 써 주세요.</p><button className="button button-primary" onClick={() => navigate('write')}>이야기 시작하기</button></div>}</section>
        </>}
        {section === 'mine' && <section className="page-section list-page"><div className="section-heading"><div><div className="eyebrow">YOUR LITTLE LIBRARY</div><h1>내 이야기</h1><p>당신이 시작한 모든 이야기를 모아두었어요.</p></div><button className="button button-primary" onClick={() => navigate('write')}>새 이야기 쓰기 ↗</button></div>{myStories.length ? <div className="story-grid">{myStories.map((story) => <StoryCard key={story.id} story={story} user={user} onOpen={setSelectedStory} onLike={toggleLike} />)}</div> : <div className="empty-state"><span>✦</span><h3>아직 써 내려간 이야기가 없어요</h3><p>첫 문장으로 당신의 작은 세계를 열어보세요.</p><button className="button button-primary" onClick={() => navigate('write')}>이야기 시작하기</button></div>}</section>}
        {section === 'write' && <section className="page-section write-page"><div className="section-heading"><div><div className="eyebrow">WRITE A NEW CHAPTER</div><h1>이야기 시작하기</h1><p>영어로 첫 문장을 적어주세요. 다음 장면은 스토리봇이 이어갑니다.</p></div></div><div className="write-layout"><form className="writing-panel" onSubmit={generateStory}><div className="panel-top"><span>01 / THE FIRST LINE</span><span>✦</span></div><h2>어떤 이야기를 들려줄까요?</h2><label className="prompt-label" htmlFor="story-prompt">첫 문장</label><textarea id="story-prompt" value={prompt} onChange={(event) => setPrompt(event.target.value)} required rows={5} placeholder="Once upon a time, there was a little fox who loved the stars." /><p className="field-hint">영어 첫 문장 · 기존 토크나이저 기준 최대 56토큰</p><div className="visibility-picker"><span>이야기 공개 여부</span><div className="visibility-options"><label className={visibility === 'public' ? 'chosen' : ''}><input type="radio" name="visibility" value="public" checked={visibility === 'public'} onChange={() => setVisibility('public')} />공개 <small>모두가 읽을 수 있어요</small></label><label className={visibility === 'private' ? 'chosen' : ''}><input type="radio" name="visibility" value="private" checked={visibility === 'private'} onChange={() => setVisibility('private')} />비공개 <small>나만 볼 수 있어요</small></label></div></div>{error && <p className="form-error" role="alert">{error}</p>}<button className="button button-primary button-large full" disabled={busy}>{busy ? '스토리봇이 이야기를 쓰고 있어요…' : '이야기 만들기 ✦'}</button><p className="form-footnote">완성된 이야기는 내 이야기에 자동 저장됩니다.</p></form><aside className="writing-note"><span className="note-star">✧</span><div className="eyebrow">A LITTLE NOTE</div><h3>모든 멋진 이야기는<br />작은 시작에서 태어나요.</h3><p>등장인물이나 장소를 첫 문장에 넣어보세요. 스토리봇이 상상력을 더해 그다음 장면을 만들어 줍니다.</p><div className="sample-prompt">“Once upon a time, a little bird found a shiny key.”</div><span className="note-flourish">❧</span></aside></div>{generated && <div className="result-panel"><div className="eyebrow">YOUR STORY IS READY</div><h2>{generated.title}</h2><p>이야기가 내 이야기에 저장되었어요.</p><div className="result-body">{generated.body}</div><div className="result-actions"><button className="button button-outline" onClick={() => setSelectedStory(generated)}>이야기 보기</button><button className="text-button" onClick={() => { setPrompt(''); setVisibility(''); setGenerated(null); window.scrollTo({ top: 0, behavior: 'smooth' }) }}>새 이야기 쓰기 ↗</button></div></div>}</section>}
        {section === 'account' && user && <AccountView user={user} onUpdate={(person) => { if (renderedVersion === accountVersion.current) setUser(person) }} onLoggedOut={(message) => { if (renderedVersion === accountVersion.current) loggedOut(message) }} />}
      </main>
      <footer className="site-footer"><div className="footer-inner"><div><strong>✦ StoryBot</strong><p>작은 문장, 오래 남을 이야기.</p></div><span>Made for stories worth sharing.</span></div></footer>
      {showAuth && <AuthDialog onClose={() => setShowAuth(false)} onSuccess={(person) => { switchAccount(person); setShowAuth(false); setNotice(`${person.nickname}님, 환영합니다.`); refreshStories(person) }} />}
      {selectedStory && <StoryDialog key={`${selectedStory.id}-${selectedStory.updated_at}-${selectedStory.is_public}`} story={selectedStory} user={user} onClose={() => setSelectedStory(null)} onLike={toggleLike} onUpdated={(story) => updatedStory(story, renderedVersion)} onDeleted={(id) => deletedStory(id, renderedVersion)} />}
      {error && section !== 'write' && <div className="floating-error" role="alert">{error}<button onClick={() => setError('')} aria-label="오류 닫기">×</button></div>}
    </div>
  )
}
