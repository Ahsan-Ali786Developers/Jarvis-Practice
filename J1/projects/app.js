const state = JSON.parse(localStorage.getItem('briefly-data') || '{"clients":[],"matters":[]}');
const $ = (selector) => document.querySelector(selector);
const save = () => localStorage.setItem('briefly-data', JSON.stringify(state));
const titleFor = (type) => ({adjournment:'Adjournment application', certified:'Certified copy request', bail:'Bail application'})[type] || 'Court application';
function render(){
  $('#clientCount').textContent = `${state.clients.length} client${state.clients.length === 1 ? '' : 's'}`;
  const recent = state.matters.slice(-4).reverse();
  $('#recentList').innerHTML = recent.length ? recent.map(m => `<div class="matter-item"><span class="matter-icon">${m.type[0].toUpperCase()}</span><div><strong>${m.title}</strong><small>${m.client}${m.caseNo ? ` · ${m.caseNo}` : ''}</small></div><span class="matter-date">${m.date}</span></div>`).join('') : '<div class="empty-state">Your saved drafts will appear here.<br>Start with a new application.</div>';
  $('#clientList').innerHTML = state.clients.length ? state.clients.slice().reverse().map(c => `<div class="client-row"><span class="matter-icon">${c.name[0].toUpperCase()}</span><div><strong>${c.name}</strong><small>${c.cases || 'No case number added'}</small></div></div>`).join('') : '<div class="empty-state">No clients yet. Add one while taking your next instruction.</div>';
}
function showView(view){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active-view')); $(`#${view}View`).classList.add('active-view'); document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('active',t.dataset.view===view));}
document.querySelectorAll('[data-view]').forEach(el=>el.addEventListener('click',()=>showView(el.dataset.view)));
document.querySelectorAll('[data-open="application"]').forEach(el=>el.addEventListener('click',()=>{$('#applicationType').value=el.dataset.template || 'adjournment'; $('#applicationDialog').showModal();}));
document.querySelector('[data-open="stamp"]').addEventListener('click',()=>$('#stampDialog').showModal());
$('#applicationForm').addEventListener('submit',(event)=>{if(event.submitter?.id !== 'saveApplication')return; const client=$('#applicationClient').value.trim(); const matter={title:titleFor($('#applicationType').value),type:$('#applicationType').value,client,caseNo:$('#applicationCase').value.trim(),date:new Date().toLocaleDateString(undefined,{day:'numeric',month:'short'})}; state.matters.push(matter); if(client&&!state.clients.some(c=>c.name.toLowerCase()===client.toLowerCase()))state.clients.push({name:client,cases:matter.caseNo}); save(); render(); $('#applicationForm').reset();});
$('#addClientButton').addEventListener('click',()=>{const name=prompt('Client name');if(!name?.trim())return;const cases=prompt('Case number (optional)')||'';state.clients.push({name:name.trim(),cases});save();render();});
function updateStamp(){const pages=Math.max(1,Number($('#stampPages').value)||1);const type=$('#stampType').value;const base={application:10,affidavit:20,agreement:50,copy:5}[type];$('#stampResult').textContent=`₹ ${base + (pages-1)*2}`;}
$('#stampType').addEventListener('change',updateStamp);$('#stampPages').addEventListener('input',updateStamp);$('#saveStamp').addEventListener('click',()=>{state.matters.push({title:'Stamp estimate',type:'stamp',client:$('#stampRegion').value||'Local filing',caseNo:`${$('#stampPages').value} page(s)`,date:new Date().toLocaleDateString(undefined,{day:'numeric',month:'short'})});save();render();});
$('#clearData').addEventListener('click',()=>{if(confirm('Clear all local demo data?')){state.clients=[];state.matters=[];save();render();}});$('#installButton').addEventListener('click',()=>alert('Use your browser menu and choose “Add to home screen”.'));
render();
